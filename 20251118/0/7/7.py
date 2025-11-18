import random
import struct

seq = [((random.random()), bytes(random.sample(range(5), 3)), random.randrange(10000)) for i in range(10)]

with open("71.txt", "bw+") as f1:
    for el in seq:
        f1.write(struct.pack("f3si", *el))
    with open("27.txt", "r") as f2:
        size = f1.seek(0, 2)    
        f2.seek(0)
        # не успел