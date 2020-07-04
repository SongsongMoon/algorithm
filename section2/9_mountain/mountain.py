import sys
sys.stdin = open("input.txt", "rt")

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
grid.insert(0, [0] * N)
grid.append([0] * N)
for rowArray in grid:
    rowArray.insert(0, 0)
    rowArray.append(0)

res = 0
for row in range(1,N+1):
    for column in range(1,N+1):
        if grid[row][column-1] < grid[row][column] and grid[row][column+1] < grid[row][column] and grid[row-1][column] < grid[row][column] and grid[row+1][column] < grid[row][column]:
                res += 1

print(res)

"""
if grid[row][column-1] < grid[row][column] and grid[row][column+1] < grid[row][column] and grid[row-1][column] < grid[row][column] and grid[row+1][column] < grid[row][column]:
                res += 1

----------------------------

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

if all( grid[row][column] > grid[i+dx[k]][j+dy[k]] for k in range(4) ):
    res += 1
"""