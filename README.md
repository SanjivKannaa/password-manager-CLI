# password-manager-windows



Pre-Requirements
1. Have python installed


How to set-up
1. Clone the repository
2. Run the initialize.py file
  Enter your file number (3 digit) and prefered password upon asking
3. Run the main.py file everytime you want to access any of your passwords or want to save a new password


Technologies and modules used
1. Python
2. cryptography module (python) for encryption and decryption operation
3. pickle module (python) for reading and writing into binary files
4. os module (python) for creating required files and folders


How the project works
  - The password is encrypted using the encryption key stored in 1 out of 1000 files (the user need to enter the file number during each execution)
