import EncryptText
import pass_gen
import sys
pwd = 0
"""
TO-DO:

1. Implement Encryption 
"""

# Generates custom password using gen_pass(size) from pass_gen.
def get_custom_pass():
    '''
    Gets password size, generates password and then sets that value to pwd.
    Ask if the user wants a new password, if so it simple generates a new one and repeats the process.
    '''
    global pwd
    running = True
    size = int(input("Input size/length of the password that you want\n"))
    
    while running:
        pwd = pass_gen.gen_pass(size) # gets a random password from the pass_gen file.
        print(" ") # user want new password?
        user_want_new_pass = input(f'Your generated password is | {pwd} | do you want a different one (Y/N)\n').lower()

        if user_want_new_pass == 'y':
            continue
        elif user_want_new_pass == 'n':
            return pwd
        else:
            print("please select from the original prompt")
        
def view():
    """
    Prints all of the contents of
    the passwords.txt file.
    """
    #Opens file in read mode and prints the file. (Removes all "\n")
    with open('passwords.txt', mode='r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split('|') # Prints the values in passwords.txt
            print("---------------------------------")
            print(f"User: \033[1;32;40m{user}\033[0m | Password: \033[1;31m{passw}\033[0m")
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
    running = True
    name = str(input("Input account name: "))
    while running:
        user_want_custom_pass = input('Do you want a randomly generated password (y/n)\n')
        print('')
        if user_want_custom_pass == 'Y' or user_want_custom_pass == "y":
            get_custom_pass()        
            running = False
        elif user_want_custom_pass == 'N' or user_want_custom_pass == "n":
            pwd = str(input('Input password: '))
            running = False
        elif user_want_custom_pass == 'q':
            print('')
            sys.exit("Exiting . . .")
        else:
            print('')
            print("Please select from the orgnal prompt.")
            continue
        

    with open('passwords.txt', mode='a') as f:
        f.write(name + '|' + pwd + '\n')

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
