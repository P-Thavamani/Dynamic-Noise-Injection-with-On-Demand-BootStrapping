# DNIB Framework: Dynamic Noise Injection with On-Demand Bootstrapping

## **Description**
The DNIB Framework is a privacy-preserving data processing tool that integrates Differential Privacy, Just-In-Time (JIT) Processing, and Bootstrap Resampling. It allows for controlled data access based on user authentication, ensuring sensitive information is either masked with noise or replaced with synthetic data for unauthorized users. The framework is ideal for handling datasets where privacy and scalability are paramount.

---

## **Features**
- Implements **Differential Privacy** for authentic users to obfuscate sensitive query results.
- Uses **JIT Processing** to apply precise filtering conditions dynamically.
- Applies **Bootstrap Resampling** to generate synthetic datasets for unverified users.
- Supports easy integration of CSV-based datasets.
- Scalable to larger systems with database support.

---

## **How It Works**
1. **Authentication**: Verifies user credentials via an external access control module. 
   - **Authenticated Users**: Receive differentially private outputs with minimal noise.
   - **Unauthenticated Users**: Receive synthetic data generated through bootstrap resampling.
   
2. **Data Processing Steps**:
   - **Load Dataset**: Reads CSV files from a specified directory.
   - **Preprocessing**: Cleans and prepares the dataset for analysis.
   - **JIT Filtering**: Filters the dataset based on user-defined conditions.
   - **Differential Privacy**: Applies epsilon-controlled noise for authenticated users.
   - **Synthetic Data Generation**: Creates bootstrap resamples for unauthorized access.

3. **Scalability**:
   - Replace CSV files with a relational database to handle larger datasets and real-time queries.

---

## **Steps to Use**
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/DNIB-Framework.git
   cd DNIB-Framework
   ```

2. **Install Dependencies**:
   - Ensure you have Python 3.8+ installed.
   - Install required libraries:
     ```bash
     pip install -r requirements.txt
     ```

3. **Run the GUI**:
   ```bash
   python main.py
   ```
   - The application interface will open. Provide the required inputs and start the process.

4. **Input Details**:
   - **Input Folder**: Folder containing CSV files to be processed.
   - **Output Folder**: Folder to save processed/synthetic data.
   - **Username & Token**: For authentication.
   - **JIT Query Condition**: Column and condition to filter data (e.g., `age < 30`).
   - **Noise Level (Epsilon)**: Control noise intensity (higher value = less noise).
   - **Synthetic Data Size**: Specify the number of rows for synthetic data.

---

## **File Descriptions**
1. **`main.py`**:
   - Manages the GUI, user inputs, and the execution pipeline.
   - Handles user authentication and data processing flow.
   
2. **`access_control.py`**:
   - Contains user authentication logic to validate credentials.

3. **`data_input.py`**:
   - Functions to load and validate CSV data.

4. **`preprocessing.py`**:
   - Data cleaning and preparation functions.

5. **`jit_processing.py`**:
   - Implements Just-In-Time (JIT) filtering based on user-defined conditions.

6. **`differential_privacy.py`**:
   - Adds noise to the data for authenticated users using Differential Privacy techniques.

7. **`bootstrap_resampling.py`**:
   - Generates synthetic datasets using bootstrap resampling.

8. **`data_storage.py`**:
   - Saves processed or synthetic data to the output directory.

---

## **Adding New CSV Files**
1. Place your CSV files in the input directory specified in the GUI.
2. Ensure each file has consistent formatting (e.g., headers and data types).
3. The framework will automatically process all CSV files in the directory.

---

## **Scaling to a Larger Version**
1. **Database Integration**:
   - Replace CSV file processing with database queries.
   - Use a database management system like MySQL, PostgreSQL, or MongoDB.
   - Modify `data_input.py` to connect to the database and fetch data dynamically.

2. **Real-Time Data Processing**:
   - Implement streaming data pipelines using tools like Apache Kafka.
   - Use APIs for dynamic data retrieval and processing.

3. **Cloud Deployment**:
   - Deploy the framework to cloud platforms (e.g., AWS, Azure) for enhanced scalability.
   - Use managed database services for seamless scaling.

---

## **License**
This project is licensed under the **Creative Commons Attribution-NoDerivatives 4.0 International (CC BY-ND 4.0)** license.  
**Terms**:
- You must give appropriate credit, including attribution to **P. Thavamani**, the creator of this framework.
- You may not distribute modified versions of this project.
- Commercial use is permitted as long as the above conditions are met.

For detailed license terms, see the `LICENSE` file.

---

## **Credits**
- Developed by **P. Thavamani**.  
- Contributions and suggestions are welcome. Please fork and submit pull requests!  

**Contact**: [thavamani.thavamani123@gmail.com](mailto:thavamani.thavamani123@gmail.com)  
