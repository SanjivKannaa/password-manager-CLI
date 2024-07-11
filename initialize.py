# init.py
import os
os.system("pip install cryptography")
from cryptography.fernet import Fernet
import pickle
import time

#####################################################################
# creating the key files
for i in range(1, 50000):
    path = 'file' + str(i) + '.bin'
    f = open(path, 'wb')
    data = [Fernet.generate_key()]
    pickle.dump(data, f)
    f.close()

print('key generation done !')


time.sleep(2)


#####################################################################
# puting master pass and inputing data

path_source = input('enter the file number (1-50000): ')
path = ''
path = 'file' + str(path_source) + '.bin'




def encry(data):
    f = open(path, 'rb')
    key = pickle.load(f)[0]
    f.close()
    fernet = Fernet(key)
    return fernet.encrypt(data.encode())


def decry(data):
    f = open(path, 'rb')
    key = pickle.load(f)[0]
    f.close()
    fernet = Fernet(key)
    return fernet.decrypt(data).decode()


f = open('master_pass.bin', 'wb')
master_key = input('whats the master password? : ')
master_key_e = encry(master_key)
master_key_d = decry(master_key_e)
print("master pass check", end=" -> ")
print(master_key == master_key_d)


pickle.dump([master_key_e], f)
f.close()


f = open('data.bin', 'wb')
data = [
    ['website', 'username', 'P@$$w0rD']
]


final = []
for i in data:
    fin = []
    for j in i:
        fin.append(encry(j))
    final.append(fin)
pickle.dump(final, f)
f.close()
print('DONE!')