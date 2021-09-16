import EncryptText
import pass_gen
pwd = 0
"""
TO-DO:

1. Add comments 
2. Implement Encryption 
"""

# Generates custom password using gen_pass(size) from pass_gen.
def get_custom_pass():
    global pwd
    running = True
    
    while running:
        '''
        Gets password size, generates password and then sets that value to pwd.
        Ask if the user wants a new password, if so it simple generates a new one and repeats the process.
        '''
        size = int(input("Input size/length of the password that you want\n"))
        pwd = pass_gen.gen_pass(size)
        user_want_new_pass = input(f'Your generated password is {pwd}  dow you want a different one (Y/N)\n')
        
        if user_want_new_pass == 'Y':
            continue
        elif user_want_new_pass == 'N':
            return pwd
        else:
            print(f"you entered {user_want_new_pass}  please use the original prompt (Y/N)\n")
            continue 
            

def view():

    # Opens file in read mode and prints the file. (Removes all "\n")

    with open('passwords.txt', mode='r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split('|')
            print("---------------------------------")
            print("User", user, '| Password ' + passw)
            print('---------------------------------')

def add():
    '''
    Gets account name.
    Ask user if they want a randomly generated password. (See "get_custom_pass()")
    after the password is generated, it opens the file writes "name" and "pwd" with a | inbetween.

    If the user donsn't want a random password, user will input a password
    opens file and does the same as it would with a random password, exept pwd = user's input.
    '''
    global pwd
    name = str(input('Input account name\n'))
    user_want_custom_pass = input('Do you want a randomly generated password (Y/N)\n')
    
    if user_want_custom_pass == 'Y':
        get_custom_pass()
        with open('passwords.txt', mode='a') as f:
            f.write(name + '|' + pwd + '\n')
    
    elif user_want_custom_pass == 'N':
        pwd = str(input('Input password\n'))
        with open('passwords.txt', mode='a') as f:
            f.write(name + '|' + pwd + '\n')
    else:
        print('An unknown error occured.')


while True:
    print("Would you like to add a new password or view existing ones?")
    mode = input("add, view, or q to quit.\n")
    
    if mode == 'q':
        break

    if mode == 'add':
        add()

    elif mode == 'view':
        view()
    else:
        print('Please select from the orginal prompt.')
        continue 
