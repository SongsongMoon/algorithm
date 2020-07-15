import sys
sys.stdin = open("input.txt", "rt")

L = int(input())
arr = list(map(int, input().split()))
M = int(input())

arr.sort()

for _ in range(M):
    arr[L-1] -= 1
    arr[0] += 1
    arr.sort()

print(arr[L-1] - arr[0])
