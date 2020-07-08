import sys
sys.stdin = open("input.txt", "rt")

def countLine(length):
    cnt = 0 
    for line in arr:
        cnt += line // length
    return cnt

K, N = map(int, input().split())
arr = sorted([int(input()) for _ in range(K)])

low = 1
height = arr[K-1] - 1
maxLength = -1

while low <= height:
    mid = (low + height) // 2
    cntLines = countLine(mid)
    if N <= cntLines:
        if N == cntLines:
            maxLength = mid
        low = mid + 1
    elif N > cntLines:
        height = mid - 1


print(maxLength)
"""
188 ~ 249
218 ~ 249
233 ~ 249

"""