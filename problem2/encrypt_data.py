from pyspark.sql import SparkSession
from pyspark.sql.functions import col, udf
from pyspark.sql.types import StringType
from cryptography.fernet import Fernet
import os

def load_key(key_file='secret.key'):
    """Load the Fernet key from a file."""
    return open(key_file, 'rb').read()

def encrypt_value(value, key):
    """Encrypt a value using the provided key."""
    fernet = Fernet(key)
    return fernet.encrypt(value.encode()).decode()

def anonymize_csv(input_file: str, key: str):
    """Anonymizes specific columns in the CSV file using encryption."""
    spark = SparkSession.builder \
        .appName("Anonymize CSV") \
        .getOrCreate()

    # Broadcast the key to all nodes
    broadcast_key = spark.sparkContext.broadcast(key)

    df = spark.read.csv(input_file, header=True, inferSchema=True)

    encrypt_udf = udf(lambda x: encrypt_value(x, broadcast_key.value), StringType())

    df_anonymized = df.withColumn("first_name", encrypt_udf(col("first_name"))) \
                      .withColumn("last_name", encrypt_udf(col("last_name"))) \
                      .withColumn("address", encrypt_udf(col("address")))

    df_anonymized.write.csv('anonymized_output.csv', header=True, mode='overwrite')
    df_anonymized.show(truncate=False)  #
    spark.stop()
    print("Data encrypted and saved to anonymized_output.csv")

if __name__ == "__main__":
    key = load_key()  # Load existing key
    anonymize_csv('input.csv', key.decode())
