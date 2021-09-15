running = True 

print

# Gets user prompt
def user_prompt():

    user_want_pass = str(input('Generate Password? (Y/N)\n'))
    
    if user_want_pass == 'Y':
        return True
    elif user_want_pass == 'N':
        False 
    else:
        print('Please select from the orginal prompt.')
        user_prompt()

while running:
    user_prompt()
    if user_prompt() == True:
        pass
    elif user_prompt() == False
