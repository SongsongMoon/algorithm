import sys
sys.stdin = open("input.txt", "rt")

arr = list(range(1,21))
for _ in range(10):
    ai, bi = list(map(int, input().split()))
    for i in range((bi-ai+1)//2):
        arr[ai+i-1], arr[bi-i-1] = arr[bi-i-1], arr[ai+i-1]
 
print(arr)

#list(range(1,21))
#switching -> a, b = b, a