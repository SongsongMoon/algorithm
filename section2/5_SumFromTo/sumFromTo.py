import sys
sys.stdin = open("input.txt", "rt")

cntArr, targetSum = map(int, input().split())
arr = list(map(int, input().split()))

res = 0
for i in range(cntArr-1):
    for j in range(i, cntArr + 1):
        print(i, j, sum(arr[i:j]))
        if sum(arr[i:j]) == targetSum:
            res += 1
            break
        elif sum(arr[i:j]) > targetSum:
            break

print(res)

"""
a = ['a', 'b', 'c', 'd', 'e']
a[ 2 : 4 ]
>>>['c', 'd']

a[ 1 : 5 ]
>>>['b', 'c', 'd', 'e']
"""

"""
[not using break] test case : 501498
[using break] test case : 34222
더 이상 필요없는 계산은 하지 않아야 효율을 높임.
"""