#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Write your code here
    m = len(player)
    n = len(ranked)
    # ref
    rank = 1
    ref_ranked = [1]
    i_r= n-1
    out = []
    for i in range(1,n):
        if(ranked[i-1]>ranked[i]):
            rank += 1
        ref_ranked.append(rank)
    ref_ranked.append(rank+1)
    for i in range(m):
        for j in range(i_r,-1,-1):
            if(ranked[j]>player[i]):
                out.append(ref_ranked[j+1])
                i_r = j
                break
            elif(j==0):
                out.append(1)
   

    return out
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
