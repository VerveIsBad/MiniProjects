import random

chars = ['!', '@', '#', '$', '%', '^', '&', '*','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


"""
0-7 = ! @ # $ % ^ & *
8 - 33 = lowercase characters.
34 - 59 = upercase characters
"""

def gen_pass(size):
    """
    Generate random password
    """
    return ''.join([random.choice(chars) for i in range(size)]) # converts to string
