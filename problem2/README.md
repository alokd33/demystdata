# Project Documentation: PySpark Data Anonymization

## Project Overview
This project aims to anonymize personal data in a CSV file by encrypting specific columns (first_name, last_name, and address) using the Fernet symmetric encryption method from the `cryptography` library. The project is structured to work with large datasets (up to 2GB), leveraging the distributed computing capabilities of Apache Spark. The process involves generating a key, encrypting the data, and then decrypting it for validation.

## How It Works (Text Diagram)
Generate Key: └─ generate_key.py → Generates a symmetric key and stores it in secret.key.

Encrypt Data: └─ encrypt_data.py → Reads input.csv, encrypts specified columns, and saves to anonymized_output.csv.

Decrypt Data: └─ decrypt_data.py → Reads anonymized_output.csv, decrypts the data using the key, and displays it.

Bash Script: └─ anonymize.sh → Orchestrates the process, logs results, and handles errors.

## How to Build Docker
1. Create a new directory:
```bash
mkdir docker_problem2
```
2. Change to that directory
```bash
cd docker_problem2
```
3. Clone the repository
```bash
git clone https://github.com/alokd33/demystdata.git
```
4. Change to the project directory:
```bash
cd demystdata/problem2
```
5. To build the Docker image for this project, run the following command in your terminal:
```bash
docker build --no-cache -t pyspark_anonymize .
```
## How to Run Docker
```bash
docker run -it --name "anonymize_process" pyspark_anonymize
```
This command will execute the anonymize.sh script, which handles the key generation, data encryption, and decryption processes.

## How to Validate the Output
After running the Docker container, you can validate the output by checking the contents of the anonymized CSV file:
```bash
cat anonymized_output.csv/part*.csv
```

To verify the decryption process, you can run the decryption script directly within the container:
```bash
spark-submit --master local[1] --driver-memory 1G --executor-memory 1G --executor-cores 1 --num-executors 1 decrypt_data.py
```
This command will display the decrypted DataFrame.

## Expected Results

1. After running the anonymization process, the anonymized_output.csv should contain encrypted values for the specified columns.
2. The decryption process should restore the original values, which can be verified by comparing the decrypted output with the original input.csv.




