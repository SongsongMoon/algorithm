import sys
sys.stdin = open("input.txt", "rt")

firstCnt = int(input())
firstArr = list(map(int, input().split()))
secondCnt = int(input())
secondArr = list(map(int, input().split()))

#print(sorted(firstArr + secondArr))
p1, p2 = 0, 0
res = []
while p1 < firstCnt and p2 < secondCnt:
    if firstArr[p1] <= secondArr[p2]:
        res.append(firstArr[p1])
        p1 += 1
    else:
        res.append(secondArr[p2])
        p2 += 1

if p1 < firstCnt:
    res += firstArr[p1:]

if p2 < secondCnt:
    res += secondArr[p2:]

print(res)