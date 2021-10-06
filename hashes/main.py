import hashlib
target = "a532443f3e04a9e00295a8cd2a75e080" # target hash
with open("sample.txt", 'rb') as f: # opens file in "Read bytes"
    for line in f: # for line in file, it hash's the line 
        # and compares its hexidecimanl value to the target.
        result = hashlib.md5(line)
        hexi = result.hexdigest()

        if hexi.lower() == target:
            print(True)
            print(line.decode())
        else:
            print(False)
    



 

