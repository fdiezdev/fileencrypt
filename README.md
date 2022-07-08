# 🔒 FileEncrypt
_Open source file encryption software_

This code consts of two files:
* `encrypt.py`
* `decrypt.py`

## How to use
✅ You should contain all the files you want to encrypt in a folder. For instance:  

`Folder1`  
|  
|--- `file.txt`  
|--- `Spreadsheet.xlsx`  
|--- `image.png`  

❌ You shouldn't contain an other folder inside of the parent folder.  
`Folder1`  
|  
|--- `Folder2`  
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|--- `example.pdf`  
|--- `file.txt`  
|--- `Spreadsheet.xlsx`  
|--- `image.png`  
The program will return an error. if you wish to encrypt a folder, zip it and place the zip in the parent folder.

Once your environment is set up, you can run the script.  
`$ python3 encrypt.py`  
The program will start. *Make sure you have python3 installed*

On startup, the program will ask you for the location of the folder containing the files to encrypt. Make sure to write the exact location of the parent folder:  
* In linux: `/home/username/Desktop/Folder1`  
* In windows: `C:\\Username\\Desktop\\Folder1`

Once you provided the file path, it will ask you if you are sure to proceed. If you answer `y` it will continue. Otherwise, it wont.
If you selected `y`, the program will generate a 'key'. This key shall remain kept secret and safely stored, because:  
* The files can be decrypted *ONLY* with this key.  
* Anyone with the key can decrypt and access the files.  
