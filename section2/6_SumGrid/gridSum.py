import sys
sys.stdin = open("input.txt", "rt")

cntCase = int(input())

grid = [[0] * cntCase] * cntCase
for i in range(cntCase):
    grid[i] = list(map(int, input().split()))

max = -272000000
for row in range(cntCase):
    sumRDiagonal = sumLDiagonal = sumRow = sumColumn = 0
    
    for column in range(cntCase):
        if row == column:
            sumRDiagonal += grid[row][column]
        elif row+column == cntCase-1:
            sumLDiagonal += grid[row][column]
            
        sumRow += grid[row][column]
        sumColumn += grid[column][row]

    if max < sumRow:
        max = sumRow

    if max < sumColumn:
        max = sumColumn

    if max < sumRDiagonal:
        max = sumRDiagonal

    if max < sumLDiagonal:
        max = sumLDiagonal

print(max)

"""
(0,0) (0,1) (0,2) (0,3) (0,4)
(1,0) (1,1) (1,2) (1,3) (1,4)
(2,0) (2,1) (2,2) (2,3) (2,4)
(3,0) (3,1) (3,2) (3,3) (3,4)
(4,0) (4,1) (4,2) (4,3) (4,4)
"""

        

