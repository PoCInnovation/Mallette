#!/bin/python3.6

import random
import string

f = open("user", "w")

for i in range(0, 100):
    f.write("User-" + str(i) + "|" + str(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))) + "\n")
f.close()
