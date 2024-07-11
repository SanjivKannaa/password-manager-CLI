import time
from cryptography.fernet import Fernet
import pickle
import os

os.system('color A')

path_source = input('enter the file number : ')
path = ''
path = 'file' + str(path_source) + '.bin'

def encry(data):
    try:
        f = open(path, 'rb')
        key = pickle.load(f)[0]
        f.close()
        fernet = Fernet(key)
        return fernet.encrypt(data.encode())
    except:
        return False

def decry(data):
    try:
        f = open(path, 'rb')
        key = pickle.load(f)[0]
        f.close()
        fernet = Fernet(key)
        return fernet.decrypt(data).decode()
    except:
        return False
      
def get_master_pass():
    f = open('master_pass.bin', 'rb')
    content = decry(pickle.load(f)[0])
    f.close()
    return content

def option1():
    f = open('data.bin', 'rb')
    content = pickle.load(f)
    f.close()
    final = []
    final.append(input('website : '))
    final.append(input('username : '))
    final.append(input('password : '))
    for i in content:
        if decry(i[0]) == final[0]:
            if decry(i[1]) == final[1]:
                return False
    en_final = []
    for i in final:
        en_final.append(encry(i))
    content.append(en_final)
    f = open('data.bin', 'wb')
    pickle.dump(content, f)
    f.close()
    return True

def option2():
    f = open('data.bin', 'rb')
    content = pickle.load(f)
    f.close()
    final = []
    for i in content:
        to_add = []
        for j in i:
            to_add.append(decry(j))
        final.append(to_add)
    for i in final:
        for j in i:
            print(j, end = '\t')
        print()

def option3():
    f = open('data.bin', 'rb')
    content = pickle.load(f)
    f.close()
    final = []
    for i in content:
        to_add = []
        for j in i:
            to_add.append(decry(j))
        final.append(to_add)
    which = input('website to change : ')
    username = input('please enter the username : ')
    found = False
    for i in final:
        if i[0] == which:
            if i[1] == username :
                i[2] = input('Enter the new password')
                found = True
    content = []
    for i in final:
        to_add = []
        for j in i:
            to_add.append(encry(j))
        content.append(to_add)
    f = open('data.bin', 'wb')
    pickle.dump(content, f)
    f.close()
    return found

def change_master_key(master_key_1, master_key_2):
   if master_key_1 == master_key_2:
       f = open('master_pass.bin', 'wb')
       pickle.dump([encry(master_key_1)], f)
       f.close()
       return True


def take_backup():
    f = open('data.bin', 'rb')
    content = pickle.load(f)
    f.close()
    del f
    f = open('backup.bin', 'wb')
    pickle.dump(content, f)
    f.close()
    return True
    
def restore_backup():
    f = open('backup.bin', 'rb')
    content = pickle.load(f)
    f.close()
    del f
    f = open('data.bin', 'wb')
    pickle.dump(content, f)
    f.close()
    return True

while True:
    password = input('enter master_password : ')
    if get_master_pass() == password:
        while True:
            print('options : \n1. add new password\n2. fetch passwords \n3. change password \n4. change master password \n5. take backup \n6. restore backup\n99. exit')
            request = input('\n >>')
            if request == '1':
                print(option1())
            elif request == '2':
                option2()
            elif request == '3':
                print(option3())
            elif request == '4':
                print(change_master_key(master_key_1 = input('enter the new master key : '), master_key_2 = input('enter the new master key : ')))
            elif request == '5':
                take_backup()
            elif request == '6':
                restore_backup()
            elif request == '99':
                exit()
            else:
                print('not valid')
    else:
        print('incorrect master_password')