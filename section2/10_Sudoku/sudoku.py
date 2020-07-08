import sys
sys.stdin = open("input.txt", "rt")

def check(arr):
    for i in range(9):
        checkRow = [0] * 10
        checkColumn = [0] * 10

        for j in range(9):
            checkRow[arr[i][j]] = 1
            checkColumn[arr[j][i]] = 1
        
        if sum(checkRow) != 9 or sum(checkColumn) != 9:
            return False
    
    for i in range(3):
        for j in range(3):
            checkRect = [0] * 10

            for k in range(3):
                for s in range(3):
                    checkRect[a[i*3+k][j*3+s]] = 1
            if sum(checkRect) != 9:
                return False
    
    return True

a = [list(map(int, input().split())) for _ in range(9) ]
if check(a):
    print('YES')
else:
    print('NO')

"""
1. (0,0) ~ (2,2)
2. (0,3) ~ (2,5)
3. (0,6) ~ (2,8)

4. (3,0) ~ (5,2)
5. (3,3) ~ (5,5)
6. (3,6) ~ (5,8)

7. (6,0) ~ (8,2)
8. (6.3) ~ (8,5)
9. (6.6) ~ (8,8)



for i in range(startRow, endRow):
    for j in range(startColumn, endColumn):

"""