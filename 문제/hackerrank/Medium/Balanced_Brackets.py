#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    brackets = []
    n = len(s)
    result = 'YES'
    for i in range(n):
        if(s[i] == '[' or s[i] == '(' or s[i] == '{'):
            brackets.append(s[i])
        else :
            if(len(brackets)==0):
                result = 'NO'
                break
            v = brackets.pop()
            if(v== '(' and s[i] != ')'):
                result = 'NO'
                break
            elif(v== '[' and s[i] != ']'):
                result = 'NO'
                break
            elif(v == '{' and s[i] != '}'):
                result = 'NO'
                break

    if(len(brackets)> 0):
        result = 'NO'
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
