import os
from cryptography.fernet import Fernet

# File to store passwords
PASSWORD_FILE = "passwords.txt"
KEY_FILE = "key.key"

# Function to generate encryption key (only needs to be run once)
def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)

# Function to load encryption key
def load_key():
    return open(KEY_FILE, "rb").read()

# Function to encrypt a password
def encrypt_password(password):
    key = load_key()
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode())
    return encrypted_password

# Function to decrypt a password
def decrypt_password(encrypted_password):
    key = load_key()
    f = Fernet(key)
    decrypted_password = f.decrypt(encrypted_password).decode()
    return decrypted_password

# Function to load stored passwords from file
def load_passwords():
    if not os.path.exists(PASSWORD_FILE):
        return {}
    with open(PASSWORD_FILE, "r") as file:
        passwords = {}
        for line in file:
            account, password = line.strip().split(" - ")
            passwords[account] = password
        return passwords

# Function to save passwords to the file
def save_passwords(passwords):
    with open(PASSWORD_FILE, "w") as file:
        for account, encrypted_password in passwords.items():
            file.write(f"{account} - {encrypted_password.decode()}\n")

# Function to add a new password
def add_password(passwords):
    account_name = input("Enter the name of the account: ")
    password = input("Enter the password: ")
    encrypted_password = encrypt_password(password)
    passwords[account_name] = encrypted_password
    save_passwords(passwords)
    print(f"Password for {account_name} added successfully.")

# Function to retrieve a password
def get_password(passwords):
    account_name = input("Enter the name of the account: ")
    if account_name in passwords:
        decrypted_password = decrypt_password(passwords[account_name])
        print(f"Password for {account_name}: {decrypted_password}")
    else:
        print("Account not found.")

# Function to authenticate the user
def authenticate():
    master_password = "mmabiaa"  # hardcoded for simplicity
    password = input("Enter the master password: ")
    if password != master_password:
        print("Invalid password. Access denied.")
        return False
    return True

# Main menu function
def main():
    # Ensure that the encryption key exists
    if not os.path.exists(KEY_FILE):
        print("Generating encryption key...")
        generate_key()
        print("Encryption key generated.")
    
    passwords = load_passwords()

    if not authenticate():
        return

    while True:
        print("\nPassword Manager")
        print("1. Add Password")
        print("2. Get Password")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_password(passwords)
        elif choice == "2":
            get_password(passwords)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the app
if __name__ == "__main__":
    main()
