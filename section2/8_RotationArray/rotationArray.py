import sys
sys.stdin = open("input.txt", "rt")

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
M = int(input())

for _ in range(M):
    row, direction, amount = map(int, input().split())
    if direction == 0:
        for _ in range(amount):
            grid[row-1].append(grid[row-1].pop(0))
    else:
        for _ in range(amount):
            grid[row-1].insert(0, grid[row-1].pop())
        
s = 0
e = N - 1

res = 0
for i in range(N):
    if i < (N // 2):
        for j in range(s,e+1):
            res += grid[i][j]
        s += 1
        e -= 1
    else:
        for j in range(s, e+1):
            res += grid[i][j]
        s -= 1
        e += 1

print(res)
# pop(0), pop()
