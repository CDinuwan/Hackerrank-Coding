s = input()
s_list = s.split(' ')
final_list = []
space = ' '
for w in s_list:
    final_list.append(w.capitalize())
print(space.join(final_list))


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    full_name = s.split(' ')
    fl=[]
    space=' '
    for w in full_name:
        fl.append(w.capitalize())
    p= space.join(fl)
    return p 

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
