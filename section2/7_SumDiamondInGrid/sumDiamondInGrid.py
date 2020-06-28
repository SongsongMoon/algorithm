import sys
sys.stdin = open("input.txt", "rt")

cntTest = int(input())
grid = [list(map(int, input().split())) for _ in range(cntTest)]

columnStartIdx = columnEndIdx = cntTest // 2

sum = 0 
for i in range(cntTest):
    for j in range(columnStartIdx, columnEndIdx+1):
        sum += grid[i][j]
    
    if i < cntTest//2:
        columnStartIdx -= 1
        columnEndIdx += 1
    else:
        columnStartIdx += 1
        columnEndIdx -= 1
print(sum)

"""
            (0,2) 
      (1,1) (1,2) (1,3)
(2,0) (2,1) (2,2) (2,3) (2,4)
      (3,1) (3,2) (3,3)
            (4,2)

"""
