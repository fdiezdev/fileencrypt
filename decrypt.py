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
 DecryptingMode
''')

def load_key():
    return open("key.fsm", "rb").read()

def decrypt_it_bitch(items, key):
    f = Fernet(key)

    for item in items:
        with open(item, 'rb') as file:
            file_recover_data = file.read()
        
        recovered_data = f.decrypt(file_recover_data)

        with open(item, 'wb') as file:
            file.write(recovered_data)

if __name__ == "__main__":
    # path_to_decrypt = "/home/fdiez/Desktop/EncryptMe"
    path_to_decrypt = input(" Provide the path to decrypt: ")

    items = os.listdir(path_to_decrypt)
    full_path = [path_to_decrypt+'/'+item for item in items]

    key = getpass(" Paste your decrypting key: ")

    decrypt_it_bitch(full_path, key)

    print('''
 =========================================================
 | 🔓 Your files are now decrypted.                      |
 =========================================================
    ''')

