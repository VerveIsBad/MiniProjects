import random

chars = ['!', '@', '#', '$', '%', '^', '&', '*','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
password = []

"""
0-7 = ! @ # $ % ^ & *
8 - 33 = lowercase characters.
34 - 59 = upercase characters
"""

def gen_pass(size):
    '''
    adds a random character to 'password' times 'size'
    '''
    password_STR = ""
    for i in range(size):
        password.append(random.choice(chars))
    return password_STR.join(password) # converts to string
