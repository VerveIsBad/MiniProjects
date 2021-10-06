import hashlib
target = "a532443f3e04a9e00295a8cd2a75e080" # target hash

# Line 55 == Golduck

with open("test.txt", "r") as f:
    for line in f:
        print(line)
        if str(line) == "Golduck":
            print(True)
            break 


 

