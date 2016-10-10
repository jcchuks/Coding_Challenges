#!/bin/python
'''Given a number of dollars, N, and a list of dollar values for C = {C0,C1,C2,...CM}  distinct coins, M, find
and print the number of different ways you can make change for N dollars if each coin is available in an infinite quantity.'''

import sys
 
def make_change(coins, n): 
    result = dfs(coins,n)  
    return result


def dfs(coins,n): 
    array = [0 for x in range(n+1)]
    array[0] = 1
    matrix = [array[:] for x in range(len(coins) + 1)]
    for i in range(1,len(coins) + 1):
        for j in range(1,n+1):
            if j >= coins[i-1]:
                matrix[i][j] = matrix[i][j- coins[i-1]] + matrix[i-1][j]
            else :
                matrix[i][j] = matrix[i-1][j]
    return matrix[len(coins)][n]
    
n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
coins = map(int,raw_input().strip().split(' '))
print make_change(coins, n)
