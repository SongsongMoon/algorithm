import sys
sys.stdin = open("input.txt", "rt")

time = '07:05:45PM'

h, m, s = map(int, time[:-2].split(':'))
print(h,m,s)
print(time[-2:].upper())
"""
grid = [list(map(int, input().split())) for _ in range(9)]

cntSudoku = 1

for i in range(9):
    for j in range(9):
        sR = ((cntSudoku%3)-1) * 3
        sC = (cntSudoku-1) * 3

"""