import sys
sys.stdin = open("input.txt", "rt")

timestamp = [1,2,2,3,4,5,6,6,13,16]
timestamp_count = len(timestamp)
top = [10,15]

def requestsServed(timestamp, top):
    # Write your code here
    servedRequestIdx = []
    for t in top:
        cntServed = 0
        filteredTimestamp = [s for i, s in enumerate(timestamp) if i not in servedRequestIdx]

        for i, request in enumerate(filteredTimestamp[::-1]):
            if cntServed >= 5:
                break
            elif request <= t:
                cntServed += 1
                servedRequestIdx.append(len(filteredTimestamp)-i-1)
        
    return len(servedRequestIdx)

print(requestsServed(timestamp, top))

"""
space = [2,5]
space_count = len(space)
x = 2

def segment(x, space):
    max = -1
    for i in range(space_count-x+1):
        minima = min(space[i:i+x])
        if max < minima:
            max = minima
    return max

print(segment(x,space))
"""

"""
N, M = map(int, input().split())
arr = list(map(int, input().split()))

def countDVD(capacity):
    sum = 0
    cnt = 1
    for music in arr:
        if sum + music > capacity:
            cnt += 1
            sum = music
        else:
            sum += music
    return cnt

N, M = map(int, input().split())
arr = list(map(int, input().split()))

low = 1
high = sum(arr)
minCapacity = -1
while low <= high:
    mid = (low + high) // 2
    if countDVD(mid) <= M:
        high = mid - 1
        minCapacity = mid
    elif countDVD(mid) > M:
        low = mid + 1

print(minCapacity)
"""
