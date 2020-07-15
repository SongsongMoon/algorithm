import sys
sys.stdin = open("input.txt", "rt")

def count(dist):
    cnt = 1
    ep = arr[0]

    for i in range(1,N):
        if arr[i] - ep >= dist:
            cnt += 1
            ep = arr[i]
    
    return cnt

N, C = map(int, input().split())
arr = sorted([int(input()) for _ in range(N)])

"""
1,2,4,8,9
"""

low = 1
high = arr[N-1]

max = -1
while low <= high:
    mid = (low+high) // 2

    if count(mid) >= C:
        max = mid
        low = mid + 1
    else:
        high = mid - 1

print(max)