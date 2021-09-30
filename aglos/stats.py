import math
import statistics
players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]
test = [34,1,46,3,1,46,8,2,4,56,2,346,3]
def mean(data):
    """
    Returns the Mean of a list of intgers
    """
    total = 0
    for i in range(len(data)):
        total += data[i]
    
    return total/len(data)

def median(data):
    """
    Returns the Median of a list of values
    !!!MUST BE A LIST OF INTEGERS ONLY!!!
    Sorts the list in assending order first.
    """
    sortList(data,0)
    n = len(data)
    index = n // 2

    if n % 2: # with an odd amount of values
        return data[index]

    elif not n % 2: # with an even amount of values 
        return mean(data[index - 1:index + 1])

def variance(data, ddof=0):
    """
    Given a list of integers
    It first gets the mean, and then calculates variance
    """
    n = len(data)
    return sum((x - mean(data)) ** 2 for x in data) / (n - ddof)

def stdev(data):
    """
    Given a list of integers
    it gets the variance and calculates Standard deviation
    """
    var = variance(data)
    st_dev = math.sqrt(var)
    return st_dev

def sortList(data, Type):
    """
    (Selection sort)
    Given a list of integers, it sorts the list in 2 ways
    Type = 0, Accending. (1,2,3,4...)
    Type = 1, Decending. (100,99,98...)
    """
    if Type == 0:
        for i in range(len(data)):
            for j in range(len(data)):
                if data[i] < data[j]: # If true, it swaps that values.
                    data[i], data[j] = data[j], data[i]
    elif Type == 1:
        for i in range(len(data)):
            for j in range(len(data)):
                if data[i] > data[j]: # If true, it swaps the values.
                    data[i], data[j] = data[j], data[i]        
    return data



print('-------------------')
print(median(test))
print(statistics.median(test))
print('-------------------')
print(mean(test))
print(statistics.mean(test))
print('-------------------')
print(variance(test))
print(statistics.variance(test))
print('-------------------')
print(stdev(test))
print(statistics.stdev(test))
print('-------------------')