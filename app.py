from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open(key.key, 'wb') as key_file:
        key_file.write(key)'''



def load_key():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    return key


master_pwd = input('What is the master password?: ')
key = load_key() + master_pwd.encode
fer = Fernet(key)

def view():
    with open('passwords.txt', mode='r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split('|')
            print("User", user, '| Password ', 
                fer.decrypt(passw.encode()))

def add():
    name = str(input('Input account name:'))
    pwd = str(input('Input password: '))

    with open('passwords.txt', mode='a') as f:
        f.write(name + '|' + fer.encrypt(pwd.encode()).decode + '\n')


while True:
    mode = input("Would you like to add a new password or view existing ones? (press q to quit): " )

    if mode == 'q':
        break

    if mode == 'add':
        add()

    elif mode == 'view':
        view()
    else:
        print('Please select from the orginal prompt.')
        continue 
