import random

running = True 
spc_chr = ['!', '@', '#', '$', '%', '^', '&', '*']
std_chr_lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
std_chr_upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
sm_pass = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18']
med_pass = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26']
lg_pass = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36']

# std_chr_lower = 'acdefghijklmnopqrstuvwxyz'.split()

"""
Note to self:

For custom sizes, just loop throught the random gen x custom size
append each value returned.
"""

#Generates password. (Based only on size for now.)
def generate_password(size):
    # Note: Size is a unused argument for now.
    global sm_pass
    global med_pass
    global lg_pass

    if size == 'small':
        """
        Gets the chr type by picking a number 1-3.
        Each character type has its own corresponding list. (i.e.  special chr's have their own, upper, lower ext)
        --------------------------------
        1 = special characyer
        2 = standard character lowercase
        3 = standard character uppercase
        --------------------------------
        Function will then select the size value based on the user's input (Small, Medium, Large)
        It will loop through that list, replaxing each value with one of the random values.
        """
        for i in range(len(sm_pass)):
            chr_type = random.randint(1,3)
            if chr_type == 1:
                sm_pass[i] = spc_chr[random.randint(0,7)]
            elif chr_type == 2:
                sm_pass[i] = std_chr_lower[random.randint(0,17)]
            elif chr_type == 3:
                sm_pass[i] = std_chr_upper[random.randint(0,17)]
        
        return sm_pass

    elif size == 'medium':
        
        for i in range(len(med_pass)):
        
            chr_type = random.randint(1,3)
            
            if chr_type == 1:
                med_pass[i] = spc_chr[random.randint(0,7)]
            elif chr_type == 2:
                med_pass[i] = std_chr_lower[random.randint(0,25)]
            elif chr_type == 3:
                med_pass[i] = std_chr_upper[random.randint(0,25)]
        
        return med_pass

    elif size == 'large':
        
        for i in range(len(lg_pass)):
            chr_type = random.randint(1,3)

            if chr_type == 1:
                lg_pass[i] = random.choice(spc_chr)
            elif chr_type == 2:
                lg_pass[i] = random.choice(std_chr_lower)
            elif chr_type == 3:
                lg_pass[i] = random.choice(std_chr_upper)

        return lg_pass

    else:
        return "An unkown error occured- please try again"
         


# Gets user prompt
def UserWantPass():
    while 1:
        user_want_pass = str(input('Generate Password? (Y/N)\n'))

        if user_want_pass.lower() == 'y':
            return True
        elif user_want_pass.lower() == 'n':
            return False
        else:
            print('Please select from the orginal prompt.')
            continue

user_want_pass = UserWantPass()

if user_want_pass == True:        
        
    pass_size = input("Input password size: (Small, Medium, Large.)").lower()
        
    if pass_size == 'small':
        print(''.join(generate_password(pass_size)))
    elif pass_size == "medium":
        print(''.join(generate_password(pass_size)))
    elif pass_size == 'large':
        print(''.join(generate_password(pass_size)))
    else:
        print('Please select from the prompt')
    
elif user_want_pass == False:
    pass

