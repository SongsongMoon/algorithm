import sys
sys.stdin = open("input.txt", "rt")

countOfTestCase = int(input())

for idxOfTest in range(countOfTestCase):
    n, s, e, k = map(int, input().split())
    arr = list(map(int, input().split()))
    sortedAndSlicedArr = sorted(arr[s-1:e])
    print((idxOfTest + 1), sortedAndSlicedArr[k-1])

