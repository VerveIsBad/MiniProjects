import math
players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]

def mean(data):
    n = 0
    for i in range(len(data)):
        n += data[i]
    n = n / len(data)
    return n

def median(data):
    n = len(data)
    index = n // 2
    if n % 2:
        return sorted(data)[index]
    
    return sum(sorted(data)[index - 1:index + 1]) / 2

def variance(data, ddof=0):
    n = len(data)
    mean = mean(data)
    return sum((x - mean) ** 2 for x in data) / (n - ddof)

def stdev(data):
    var = variance(data)
    st_dev = math.sqrt(var)
    return st_dev


