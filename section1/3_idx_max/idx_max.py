import sys
sys.stdin = open("input.txt", "rt")

n, k = map(int, input().split())
arr = list(map(int, input().split()))

print("n:", n, "k:", k)
print("arr:", arr)

case = set()
for i in range(0,n):
    for m in range(i+1,n):
        for j in range(m+1,n):
            case.add(arr[i] + arr[m] + arr[j])

case = list(case)
case.sort(reverse=True)
print(case)
print(case[k-1])