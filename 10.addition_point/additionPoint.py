import sys
sys.stdin = open("input.txt", "rt")

cntArr = int(input())
arr = list(map(int, input().split()))

"""
scoreArr = [0] * cntArr
totalScore = 0
for i in range(cntArr):
    if arr[i] == 1:
        if i == 0:
            scoreArr[i] += 1
        else:
            scoreArr[i] = scoreArr[i-1] + 1
                
print(sum(scoreArr))
"""

sum = 0
additionalPoint = 0
for element in arr:
    if element == 1:
        additionalPoint += 1
        sum += additionalPoint
    else:
        additionalPoint = 0
print(sum)