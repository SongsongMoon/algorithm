import sys
sys.stdin = open("input.txt", "rt")

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

cntBoat = 0
minIdx = 0
maxIdx = N-1

while minIdx <= maxIdx:
    if len(arr) == 1:
        cntBoat += 1
        break

    if arr[maxIdx] + arr[minIdx] <= M:
        maxIdx -= 1
        minIdx += 1
        cntBoat += 1
    elif arr[maxIdx] + arr[minIdx] > M:
        cntBoat += 1
        maxIdx -= 1

print(cntBoat)

