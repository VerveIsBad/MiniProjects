nums = [4,2,9,10,7,6,1]

test = [3,4,1,2,3,4,1,2,6,0]
#       0,1,2,3
'''
def sort_list(values):
    n = len(values)
    lowest = 1
    print(lowest)
    dont_use_list = []
    new_list = []
    for i in range(n):
        for count, value in enumerate(values):
            if value < lowest:
                lowest = value
                for i in range(len(dont_use_list)):
                    if count == dont_use_list[i]
                    break 
                    else:
                        dont_use_list.append(count)

            else:
                print('ew')

    new_list.append(lowest)

    
    return lowest

print(sort_list(test))
'''