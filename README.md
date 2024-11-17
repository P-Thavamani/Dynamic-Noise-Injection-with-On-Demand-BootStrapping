# DNIB Framework: Dynamic Noise Injection with On-Demand Bootstrapping  

## **Description**  
The DNIB Framework is a privacy-preserving data processing tool that integrates Differential Privacy, Just-In-Time (JIT) Processing, and Bootstrap Resampling. It allows for controlled data access based on user authentication, ensuring sensitive information is either masked with noise or replaced with synthetic data for unauthorized users. The framework is ideal for handling datasets where privacy and scalability are paramount.  

---  

## **Features**  
- Implements **Differential Privacy** for authenticated users to obfuscate sensitive query results.  
- Uses **JIT Processing** to dynamically filter data based on user queries.  
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
   - Ensure Python 3.8+ is installed.  
   - Install required libraries:  
     ```bash  
     pip install -r requirements.txt  
     ```  

3. **Run the Framework**:  
   ```bash  
   python main.py  
   ```  
   - The GUI will open. Provide the required inputs and start the process.  

4. **Input Details**:  
   - **Input Folder**: Path to the folder containing CSV files to process.  
   - **Output Folder**: Path to save processed or synthetic data.  
   - **Username & Token**: For authentication.  
   - **JIT Query Condition**: Define a filter (e.g., `age < 30`).  
   - **Noise Level (Epsilon)**: Control noise intensity (higher value = less noise).  
   - **Synthetic Data Size**: Specify the number of rows for synthetic data.  

---  

## **File Descriptions**  

1. **`main.py`**:  
   - Manages the GUI, user inputs, and execution pipeline.  
   - Handles authentication and data processing.  

2. **`access_control.py`**:  
   - Contains user authentication logic.  

3. **`data_input.py`**:  
   - Functions to load and validate CSV data.  

4. **`preprocessing.py`**:  
   - Data cleaning and preparation functions.  

5. **`jit_processing.py`**:  
   - Implements Just-In-Time (JIT) filtering.  

6. **`differential_privacy.py`**:  
   - Adds noise to the data for authenticated users.  

7. **`bootstrap_resampling.py`**:  
   - Generates synthetic datasets.  

8. **`data_storage.py`**:  
   - Saves processed or synthetic data to the output directory.  

---  

## **Adding New CSV Files**  
1. Place new CSV files in the specified input directory.  
2. Ensure consistent formatting across all files (e.g., headers, data types).  
3. The framework will automatically process all files in the directory.  

---  

## **Scaling to a Larger Version**  

1. **Database Integration**:  
   - Replace CSV files with relational databases (e.g., MySQL, PostgreSQL).  
   - Modify `data_input.py` to connect to the database dynamically.  

2. **Real-Time Data Processing**:  
   - Use streaming tools like Apache Kafka for real-time pipelines.  
   - Implement APIs for dynamic data retrieval.  

3. **Cloud Deployment**:  
   - Deploy on cloud platforms like AWS or Azure.  
   - Leverage managed database services for scalability.  

---  

## **License**  

This project is licensed under the **GNU Affero General Public License v3.0 (AGPLv3)**.  

**Key Points**:  
- Any modifications or larger works must also be licensed under AGPLv3.  
- Source code of modifications or hosted services must be made available.  
- Proper attribution to **P. Thavamani** must be maintained in all copies.  

For detailed terms, refer to the `LICENSE` file.  

---  

## **Credits**  
- Developed by **P. Thavamani**.  
- Contributions are welcome! Fork the repository and submit pull requests.  

**Contact**: [thavamani.thavamani123@gmail.com](mailto:thavamani.thavamani123@gmail.com)  
