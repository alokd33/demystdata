# Project Documentation: PySpark Data Anonymization

## Project Overview
This project aims to anonymize personal data in a CSV file by encrypting specific columns (first_name, last_name, and address) using the Fernet symmetric encryption method from the `cryptography` library. The project is structured to work with large datasets (up to 2GB), leveraging the distributed computing capabilities of Apache Spark. The process involves generating a key, encrypting the data, and then decrypting it for validation.

## Input Data
The source data is provided in `input.csv`:

```csv
first_name,last_name,address,date_of_birth
John,Doe,123 Main St,1990-01-01
Jane,Smith,456 Elm St,1985-05-15
al,test,111 Elm St,2024-05-15
```

## Sample Encrypted Data
After processing, the data is anonymized and saved in anonymized_output.csv as shown below:
```csv
first_name,last_name,address,date_of_birth
gAAAAABnFM0-LVjGEya9URtjfKcjYnBoYHbfxCXVRFLX54N-dPAz-A3ayprq7V2mc0BDfKWdMFy2cpG_K2usqdn8Mg06xY91Rg==,gAAAAABnFM0-JD5_li3e9XAIRip53dd9LG8WCQIwhV_FlpR__TqL7MZGM0Rkcrbvzlc1812FbAxwBhkFhncLba5AQG3s-bYc4w==,gAAAAABnFM0-_5eYMI9FeJ3AHKEJnajHx5Ii9HOIR7obl_Jdtw3yLoBWhfpRIdjjSj7FqI9rpkWI87WpiCC5Ba9N6B1Xac_9ew==,1990-01-01
gAAAAABnFM0-YK2KRpMUPw57RJ3MVGwQtUeSYim6CYJtLR6Q6JwbUhBg4XFV7h1r-VJhe2-ivXxxgemZA-Lfu81JGFW2YO31cg==,gAAAAABnFM0-UPxDmmbNyJmZzhx78cWwDdZxB8iT0NOPM9MNs7RGk9jzkdExfHRRBVfCFOSvqgLmBVRupdYYivXZtySpMySUMw==,gAAAAABnFM0-FazwPPRHZn_UfEzpNqF4iiyyAsDaIu0u_zpjtZnlNCLg0z6axdcbtB2pzUhl7LxYlz-xzHmQcWOTucxvdPb5Nw==,1985-05-15
gAAAAABnFM0-x1VnBPSzI5REvlSde9X4d2jAan13YHQLPMiV8fuxrFbaVcgPlpK7B4xVpx7ANkyTaxvlW16Qj06sN_t3ReubvA==,gAAAAABnFM0-cYQftZ0d4nJ_StyFXfWhV_n5S5evxUSQJNPcmdM_CmQ1qIZrjL16QKKqbW4lIj7oBtBJUXfukoHvVP3dMtOe1g==,gAAAAABnFM0-Fco7S3bFsObkYiKaajuozwsHxwctOymmE97K2nqyI0oGeUs_ieuu_FYp-81crllHXcJyudGMoepT8XiLvs2NuQ==,2024-05-15
```

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




