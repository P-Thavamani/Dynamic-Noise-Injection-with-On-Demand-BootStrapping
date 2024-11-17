import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from data_input import load_data_from_files
from preprocessing import preprocess_data
from jit_processing import jit_access_control
from differential_privacy import apply_differential_privacy
from bootstrap_resampling import bootstrap_resample
from data_storage import save_synthetic_data
from access_control import authenticate_user  # Import access control module


def get_columns(input_directory):
    """Fetch columns from the combined dataset for dropdown menus."""
    combined_data = load_data_from_files(input_directory)
    if combined_data is not None:
        return combined_data.columns.tolist()
    return []


def run_dnib(input_directory, output_directory, noise_level, file_size, jit_column, jit_symbol, jit_value, dp_column, username, token):
    # Step 1: Authenticate user
    is_verified_user = authenticate_user(username, token)

    # Step 2: Load data from files
    combined_data = load_data_from_files(input_directory)
    if combined_data is None:
        messagebox.showerror("Error", "Failed to load data from files.")
        return

    # Step 3: Preprocess the combined data
    processed_data = preprocess_data(combined_data)

    # Step 4: Apply JIT processing
    query_condition = f"{jit_column} {jit_symbol} {jit_value}"  # Combine parts into a query
    try:
        filtered_data = jit_access_control(processed_data, query_condition)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to apply JIT processing: {e}")
        return

    if is_verified_user:
        # Step 5: Process data for verified user
        try:
            query_result = filtered_data[dp_column].sum()
            noised_result = apply_differential_privacy(query_result, sensitivity=1.0, epsilon=noise_level)
            print(f"Noised Result (Verified User): {noised_result}")
        except KeyError:
            messagebox.showerror("Error", f"Column '{dp_column}' not found in the data.")
            return

        # Step 6: Save verified user's original (DP-protected) data
        save_synthetic_data(filtered_data, output_directory)
        print("Data processed and saved successfully.")
    else:
        # Step 5: Generate synthetic data for unverified users
        synthetic_data = bootstrap_resample(filtered_data, n_samples=file_size)

        # Step 6: Save synthetic data without frontend pop-ups
        save_synthetic_data(synthetic_data, output_directory)
        print("Synthetic data saved successfully.")


def select_input_folder(entry, columns_dropdown, dp_dropdown):
    folder = filedialog.askdirectory(title="Select Input Folder")
    if folder:
        entry.delete(0, tk.END)
        entry.insert(0, folder)
        # Dynamically populate column options
        columns = get_columns(folder)
        columns_dropdown["values"] = columns
        dp_dropdown["values"] = columns
        if columns:
            columns_dropdown.current(0)
            dp_dropdown.current(0)


def select_output_folder(entry):
    folder = filedialog.askdirectory(title="Select Output Folder")
    if folder:
        entry.delete(0, tk.END)
        entry.insert(0, folder)


def main_gui():
    root = tk.Tk()
    root.title("DNIB Framework with Access Control")
    window_width = 500
    window_height = 400

    # Get the screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate the position to center the window
    position_x = (screen_width - window_width) // 2
    position_y = ((screen_height - window_height) // 2) - 160

    # Set window size and position
    root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
    root.resizable(False, False)

    # Input Folder Selection
    tk.Label(root, text="Input Folder:").place(x=20, y=20)
    input_folder_entry = tk.Entry(root, width=46)
    input_folder_entry.place(x=150, y=20)
    tk.Button(root, text="Browse", command=lambda: select_input_folder(input_folder_entry, jit_column_dropdown, dp_dropdown)).place(x=440, y=14)

    # Output Folder Selection
    tk.Label(root, text="Output Folder:").place(x=20, y=60)
    output_folder_entry = tk.Entry(root, width=46)
    output_folder_entry.place(x=150, y=60)
    tk.Button(root, text="Browse", command=lambda: select_output_folder(output_folder_entry)).place(x=440, y=54)

    # Username Entry
    tk.Label(root, text="Username:").place(x=20, y=100)
    username_entry = tk.Entry(root, width=20)
    username_entry.place(x=150, y=100)

    # Token Entry
    tk.Label(root, text="Password:").place(x=20, y=140)
    token_entry = tk.Entry(root, width=20, show="*")
    token_entry.place(x=150, y=140)

    # JIT Query Condition
    tk.Label(root, text="JIT Query Condition:").place(x=20, y=180)
    jit_column_dropdown = ttk.Combobox(root, width=20, state="readonly")
    jit_column_dropdown.place(x=150, y=180)
    jit_symbol_dropdown = ttk.Combobox(root, width=3, state="readonly", values=["=", "<", ">", "<=", ">=", "!="])
    jit_symbol_dropdown.place(x=308, y=180)
    jit_symbol_dropdown.current(1)  # Default to '<'
    jit_value_entry = tk.Entry(root, width=10)
    jit_value_entry.place(x=360, y=180)
    jit_value_entry.insert(0, "10")  # Default value

    # Differential Privacy Column
    tk.Label(root, text="Differential Privacy Column:").place(x=20, y=220)
    dp_dropdown = ttk.Combobox(root, width=20, state="readonly")
    dp_dropdown.place(x=200, y=220)

    # Noise Level Slider
    tk.Label(root, text="Noise Level (Epsilon):").place(x=20, y=260)
    noise_level_slider = tk.Scale(root, from_=0.01, to=1.0, resolution=0.01, orient=tk.HORIZONTAL)
    noise_level_slider.set(0.1)
    noise_level_slider.place(x=160, y=240)

    # File Size Entry
    tk.Label(root, text="Synthetic Data Size:").place(x=20, y=300)
    file_size_entry = tk.Entry(root, width=10)
    file_size_entry.insert(0, "100")  # Default size
    file_size_entry.place(x=160, y=300)

    # Run Button
    def on_run():
        input_folder = input_folder_entry.get()
        output_folder = output_folder_entry.get()
        jit_column = jit_column_dropdown.get()
        jit_symbol = jit_symbol_dropdown.get()
        jit_value = jit_value_entry.get()
        dp_column = dp_dropdown.get()
        noise_level = float(noise_level_slider.get())
        username = username_entry.get()
        token = token_entry.get()

        try:
            file_size = int(file_size_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Synthetic data size must be an integer.")
            return

        if not os.path.exists(input_folder):
            messagebox.showerror("Error", "Input folder does not exist.")
            return
        if not os.path.exists(output_folder):
            messagebox.showerror("Error", "Output folder does not exist.")
            return
        if not jit_column or not dp_column:
            messagebox.showerror("Error", "Please select a column for JIT or Differential Privacy.")
            return

        run_dnib(input_folder, output_folder, noise_level, file_size, jit_column, jit_symbol, jit_value, dp_column, username, token)

    tk.Button(root, text="Run DNIB", command=on_run, bg="green", fg="white").place(x=230, y=340)

    root.mainloop()


if __name__ == "__main__":
    main_gui()
