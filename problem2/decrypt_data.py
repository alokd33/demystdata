from pyspark.sql import SparkSession
from pyspark.sql.functions import col, udf
from pyspark.sql.types import StringType
from cryptography.fernet import Fernet

def load_key(key_file='secret.key'):
    """Load the Fernet key from a file."""
    return open(key_file, 'rb').read()

def decrypt_value(encrypted_value, key):
    """Decrypt a value using the provided key."""
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_value.encode()).decode()

def decrypt_csv(input_file: str, key: str):
    """Decrypts the encrypted CSV data."""
    spark = SparkSession.builder \
        .appName("Decrypt CSV") \
        .getOrCreate()

    df = spark.read.csv(input_file, header=True, inferSchema=True)

    decrypt_udf = udf(lambda x: decrypt_value(x, key), StringType())

    df_decrypted = df.withColumn("first_name", decrypt_udf(col("first_name"))) \
                     .withColumn("last_name", decrypt_udf(col("last_name"))) \
                     .withColumn("address", decrypt_udf(col("address")))

    df_decrypted.show()  # Display the decrypted data
    spark.stop()

if __name__ == "__main__":
    key = load_key()  # Load existing key
    decrypt_csv('anonymized_output.csv', key.decode())