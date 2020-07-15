import sys
sys.stdin = open("input.txt", "rt")

numList, m = map(int, input().split())
numList = list(map(int, str(numList)))

stackList = []
for num in numList:
    while stackList and m > 0 and stackList[-1] < num:
        stackList.pop()
        m -= 1
    stackList.append(num)

if m != 0:
    stackList = stackList[:-m]

res = ''.join(map(str, stackList))
print(res)
