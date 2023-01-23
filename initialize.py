# init.py

import os

os.system("pip install cryptography")
from cryptography.fernet import Fernet
import pickle
import time



##################################################################
# creating binary files (without data)
f = open('data.bin', "wb")
f.close()
f = open('master_key.bin', "wb")
f.close()
















#####################################################################
# creating the bulk folders and the key files
'''
for i in range(1, 11):
    os.mkdir ('file' + str(i))

print('done level 0')







for i in range(1, 11):
    for j in range(1, 11):
        os.mkdir('file' + str(i) + '\\' + 'file' + str(j))


print('done level 1')








for i in range(1, 11):
    for j in range(1, 11):
        for k in range(1, 11):
            os.mkdir ('file' + str(i) + '\\' + 'file' + str(j) + '\\' + 'file' + str(k))
            print(str(i) + '\t' + str(j) + '\t' + str(k))
            
print('done level 2')


'''



for i in range(1, 11):
    for j in range(1, 11):
        for k in range(1, 11):
            path = 'file' + str(i) + '\\' + 'file' + str(j) + '\\'  + 'file' + str(k) + '\\'  + 'file' + '.bin'
            f = open(path, 'wb')
            data = [Fernet.generate_key()]
            pickle.dump(data, f)
            f.close()
            print(str(i) + '\t' + str(j) + '\t' + str(k) + '\t')
    




print('done !')


time.sleep(2)


#####################################################################
#puting master pass and inputing data

path_source = input('enter the file number : ')
path = ''
path = 'file' + path_source[0] + '\\file' + path_source[1] + '\\file' + path_source[2] + '\\file.bin'




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






'''
f = open('data.bin', 'wb')
f.close()





'''




f = open('master_pass.bin', 'wb')


master_key = input('whats the master_key? : ')

master_key_e = encry(master_key)

master_key_d = decry(master_key_e)


print(master_key == master_key_d)




pickle.dump([master_key_e], f)

f.close()


f = open('master_pass.bin', 'rb')
content = decry(pickle.load(f)[0])
f.close()
print(content)





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


