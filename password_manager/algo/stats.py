players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]
'''
the mean is 33.1. To calculate the variance, we take the difference between each value and the mean, square it, and then average the result: Variance = 292.5

Now we take the square root of the Variance, to get the Standard Deviation: std = 17.1

Now, we can check which ages are within one standard deviation (17.1) from the mean (33.1) - from (33.1-17.1) to (33.1+17.1):
'''



def get_mean(list):
    n = 0
    for i in range(len(list)):
        n += list[i]
    n = n / len(list)
    return n

def get_deviation(list):
    mean = get_mean(list)
    n = 0
    for count, value in enumerate(list):
        count = 0
        n += (mean - value)
    n**2
    return n

print(get_deviation(players))

