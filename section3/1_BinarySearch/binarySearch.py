import sys
sys.stdin = open("input.txt", "rt")

N, M = map(int, input().split())

arr = sorted(list(map(int, input().split())))

high = len(arr) - 1
low = 0

while high >= low:
    mid = (high + low) // 2

    if M < arr[mid]:
        high = mid - 1
    elif M > arr[mid]:
        low = mid + 1
    elif M == arr[mid]:
        print(mid + 1)
        break
    else:
        print("Not found")

