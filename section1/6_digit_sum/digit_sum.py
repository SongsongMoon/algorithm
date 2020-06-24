import sys
sys.stdin = open("input.txt", "rt")

def digit_sum(x):
    return sum(list(map(int, str(x))))

N = int(input())
arr = list(map(int, input().split()))

sumList = []
for element in arr:
    digitSum = digit_sum(element)
    sumList.append(digitSum)

max = -247000000
idx = -1
for i in range(0,N):
    if max < sumList[i]:
        max = sumList[i]
        idx = i
print(arr[idx])
