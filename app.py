master_pwd = input('What is the master password?: ')


def view():
    with open('passwords.txt', mode='r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split('|')
            print("---------------------------------")
            print("User", user, '| Password ' + passw)
            print('---------------------------------')
def add():
    name = str(input('Input account name:'))
    pwd = str(input('Input password: '))

    with open('passwords.txt', mode='a') as f:
        f.write(name + '|' + pwd + '\n')


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
