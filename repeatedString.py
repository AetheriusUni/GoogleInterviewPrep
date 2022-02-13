#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

"""
There is a string, s, of lowercase English letters that is repeated infinitely many times. 
Given an integer, n, find and print the number of letter a's in the first n letters of the infinite string.
"""

def repeatedString(s, n):
    # Write your code here
    numA = 0
    # takes care of case where number of chars to check is less than length of s
    if len(s)>n:
        for i in range(n):
            if s[i] == 'a':
                numA+=1
        return numA
    # below takes care of every other case
    # count number of s repeats
    numRepeats = n//len(s)
    # count number of chars in the last incomplete string if any
    numRemainder = n%len(s)
    # count number of 'a' in this incomplete string
    numAextra = 0
    # count number of 'a' in s
    for i in range(len(s)):
        if s[i] == 'a':
            numA+=1
            if i<numRemainder:
                numAextra+=1
    return numA*max(numRepeats, 1)+numAextra



if __name__ == '__main__':


    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    print(result)
