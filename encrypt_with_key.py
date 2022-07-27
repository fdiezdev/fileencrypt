from getpass import getpass
from cryptography.fernet import Fernet 
import os

print('''
  ______ _ _      ______                             _   
 |  ____(_) |    |  ____|                           | |  
 | |__   _| | ___| |__   _ __   ___ _ __ _   _ _ __ | |_ 
 |  __| | | |/ _ \  __| | '_ \ / __| '__| | | | '_ \| __|
 | |    | | |  __/ |____| | | | (__| |  | |_| | |_) | |_ 
 |_|    |_|_|\___|______|_| |_|\___|_|   \__, | .__/ \__|
                                          __/ | |        
                                         |___/|_|        v0.1
 ReEncryptingMode
 1. Use this tool under your own risk. The developers are not responsible for the data loss caused by users.
 2. This tool is intended to ONLY encrypt FILES, NOT FOLDERS. If you wish to encypt a folder, first you must zip it.

 This script is for using only when you already have an encryption key and you want to re encrypt your files with the same key.
''')

# Generates the encryptation key
def key_gen():
    key = input("Insert your encryption key: ");
    #with open('key.fsm', 'wb') as key_file:
    #    key_file.write(key)

# Reads the key from the fsm file and returns it
def load_key():
    return input(" Paste your key to confirm: ")
    # return open("key.fsm", "rb").read()

# Encrypts the files
def encrypt_bitch(items, key):
    f = Fernet(key)

    # Goes trough all the files in a folder
    for item in items:

        with open(item, "rb") as file:
            file_data = file.read()

        encrypted_file = f.encrypt(file_data)

        with open(item, "wb") as file:
            file.write(encrypted_file)

if __name__ == '__main__': # I dont understand this line
    
    path_to_encrypt = input(" Provide the path to encrypt: ")

    agreement = input(" Are you sure you want to proceed (y/n): ")
    if (agreement == "y"):
        # path_to_encrypt = "/home/fdiez/Desktop/EncryptMe"
        
        items = os.listdir(path_to_encrypt)

        full_path = [path_to_encrypt+'/'+ item for item in items]

        key_gen()
        key = load_key()

        encrypt_bitch(full_path, key)

        print('''
 =========================================================
 | 🔒 Your files are now encrypted.                      |
 =========================================================
        ''')
    else:
        print(" Program exited with no encryption.")