import hashlib
target = "999cae1e22fe69d89d6f56e3050f18cb" # target hash
file = "sample.txt"
def find_hash(file, target):
    """
    Given a target MD5 hash, and a file of words
    It hash's every word in the file and compares it to the target hash.
    """
    with open(file, 'r') as f:
        for line in f:
            i = line.strip("\n")
            n = i.lower()
            x = n.encode()
            test_case = hashlib.md5(x)
            hexi = test_case.hexdigest()
            if hexi == target:
                print(f"Match found: {line}")
                print(f"line = {hexi}, target = {target}")
                return n
                break


find_hash(file, target)


