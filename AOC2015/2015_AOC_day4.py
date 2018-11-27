import hashlib
from multiprocessing import Process

zero_length = 6
zero_string = "000000"
iterations = 100000000

for i in range(iterations):
    hashstring = 'yzbqklnj'
    hashstring += str(i)
    encoded = hashstring.encode('utf-8')
    md5 = hashlib.md5()
    md5.update(encoded)
    print("Running iteration ", i)
    if str(md5.hexdigest())[:zero_length] == zero_string:
        print(i)
        break
    i += 1


