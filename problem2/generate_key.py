from cryptography.fernet import Fernet

def generate_key(key_file='secret.key'):
    """Generate a new Fernet key and save it to a file."""
    key = Fernet.generate_key()
    with open(key_file, 'wb') as f:
        f.write(key)
    print(f"Key generated and stored in {key_file}")

if __name__ == "__main__":
    generate_key()
