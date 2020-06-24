"""
1,2,3,4
1,2,3,4,5,6

2,3,4,5,6,7
3,4,5,6,7,8
4,5,6,7,8,9
5,6,7,8,9,10

0 - 0
1 - 0
2 - 1
3 - 2
4 - 3
5 - 4
6 - 4
7 - 4
8 - 3
9 - 2
10 - 1
"""

import sys
sys.stdin = open("input.txt", "rt")

N,M = map(int, input().split())

sumList = [0] * (N+M+1)
for i in range(1,N+1):
    for j in range(1,M+1):
        sumList[i+j] += 1
        
max = sorted(sumList, reverse=True)[0]

for i in range(i,N+M+1):
    if max == sumList[i]:
        print(i)
