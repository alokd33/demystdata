# Project Documentation: PySpark Data Anonymization

## Project Overview
This project aims to anonymize personal data in a CSV file by encrypting specific columns (first_name, last_name, and address) using the Fernet symmetric encryption method from the `cryptography` library. The project is structured to work with large datasets (up to 2GB), leveraging the distributed computing capabilities of Apache Spark. The process involves generating a key, encrypting the data, and then decrypting it for validation.

## How It Works 

Generate Key: └─ generate_key.py → Generates a symmetric key and stores it in secret.key.

Encrypt Data: └─ encrypt_data.py → Reads input.csv, encrypts specified columns, and saves to anonymized_output.csv.

Decrypt Data: └─ decrypt_data.py → Reads anonymized_output.csv, decrypts the data using the key, and displays it.

Bash Script: └─ anonymize.sh → Orchestrates the process, logs results, and handles errors.

```plaintext
+--------------------+
|   Start Process    |
+--------------------+
          |
          v
+--------------------+
|   Generate Key     |
|  (generate_key.py) |
+--------------------+
          |
          v
+---------------------------+
|   Store Key in File       |
|   (secret.key)            |
+---------------------------+
          |
          v
+---------------------------+
|   Load Key                |
|  (in encrypt_data.py)     |
+---------------------------+
          |
          v
+----------------------------------+
|   Broadcast Key to Nodes         |
|   (spark.sparkContext.broadcast) |
+----------------------------------+
          |
          v
+---------------------------+
|   Read Input CSV          |
|  (input.csv)              |
+---------------------------+
          |
          v
+--------------------------------+
|   Encrypt Data                 |
|   (anonymize_csv)              |
|   - UDF uses broadcasted key   |
+--------------------------------+
          |
          v
+------------------------------+
|   Write Encrypted Data       |
|   (to anonymized_output.csv) |
+------------------------------+
          |
          v
+---------------------------+
|   Load Encrypted Data     |
|   (in decrypt_data.py)    |
+---------------------------+
          |
          v
+-----------------------------------+
|   Broadcast Key to Nodes          |
|   (spark.sparkContext.broadcast)  |
+-----------------------------------+
          |
          v
+------------------------------+
|   Decrypt Data               |
|   (decrypt_csv)              |
|   - UDF uses broadcasted key |
+------------------------------+
          |
          v
+-----------------------------+
|   Display Decrypted Data    |
+-----------------------------+
          |
          v
+---------------------------+
|       End Process         |
+---------------------------+
```

1. Start Process: The entire process begins.
2. Generate Key: A key is generated using the generate_key.py script.
3. Store Key in File: The generated key is saved to a file (secret.key).
4. Load Key: The key is loaded in the encrypt_data.py script.
5. Broadcast Key to Nodes: The key is broadcasted to all Spark nodes to enable efficient access.
6. Read Input CSV: The input CSV file containing sensitive data is read.
7. Encrypt Data: The specified columns are encrypted using a UDF that accesses the broadcasted key.
8. Write Encrypted Data: The encrypted data is written to a new CSV file (anonymized_output.csv).
9. Load Encrypted Data: The encrypted data is loaded in the decrypt_data.py script.
10. Broadcast Key to Nodes: The key is broadcasted again to all nodes for decryption.
11. Decrypt Data: The encrypted data is decrypted using a UDF that accesses the broadcasted key.
12. Display Decrypted Data: The decrypted data is displayed for verification.
13. End Process: The process concludes.
**Note** : In production will keep secret.key in the vault as key and value pair will have the access control on top that.

## Input Data
The source data is provided in `input.csv`:

```csv
first_name,last_name,address,date_of_birth
John,Doe,123 Main St,1990-01-01
Jane,Smith,456 Elm St,1985-05-15
al,test,111 Elm St,2024-05-15
```

## Sample Encrypted Data
After processing, the data is anonymized and saved in anonymized_output.csv as shown below (Anonymize Data will update/change based on key):
```csv
first_name,last_name,address,date_of_birth
gAAAAABnFZvCO3hKS5yHfbg75TOpWP47kqUfA-pP5esmTa1eaiOAT8F88nTyTRvwPbJT4l7CGMXHQV6GFCIzV_yF25ZfBIcz_Q==,gAAAAABnFZvCLiGD4QVjsebZqA6oe9ZtxOV9nqpAvxjq9zExNfzBwIjH3HUG5Idd8Qp6L5y2wQpK-ZMPeRjoKOOsFBkbi7Po3w==,gAAAAABnFZvC0sPIPcwiKOmZNwG8iw2mCaEehhS4CIVy-6aVB0GZZUpagQeXLk-bXeb0pdnkfHlB5UzF3OMvsSl2s5r_EpIwjw==,1990-01-01
gAAAAABnFZvCz7_uJpqdyAgMm1HqWaharOZXnHJ311_P2CJPjyoHlmJfr8WMzUfDeWLd8LItMf9u3QpKWvT1l8qminP8mT_JjQ==,gAAAAABnFZvCbzm1AtgM8XDzmd3BZziGA8GN_z3Yt2nssRCSl8PPjWnjkyddns-h5Oa1VtpQ2N3qAXhVyBySK8TXrgzxgYfH9A==,gAAAAABnFZvCnZIwT_JDz8yANq7cwdOnjM9VZLb56Kz9r0hxSH4akV3Id8A7gcJX4Y2U0i74OIXHOJN7cEWGIQkZp78ANK1mvg==,1985-05-15
gAAAAABnFZvCXx9R1BNIbSsChv_L0Quu8SQ9iN4qOlL1u_kjQlG7seIv8xhugklppYwCi5bAhdfChfaJmZEUUqxpMkF5QmtKMQ==,gAAAAABnFZvCQdj-nmM2y0z-p3DhTnnX3obeBqtBurRA4VDZJXfQU9hsNsJgJrCo1V5Y3IPhj_ZXA_WwZdJzbl7pX2HTTnJbUw==,gAAAAABnFZvCiiFpLAtyhuCVUTDRmYQ69dUaA2w3QsJtVJnPsMUfM42JpwXQk9AILCAnBej8CD6xWypQWeJq2qVJ3rlxYCtM_A==,2024-05-15
```

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




