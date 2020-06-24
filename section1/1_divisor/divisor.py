import sys
sys.stdin = open("in1.txt", "rt")

inputNumber = input()

print("input numbers : ", inputNumber)
#8
n, k = map(int, inputNumber.split())

cnt = 0
for i in range(1, n+1):
    if n%i == 0:
        cnt += 1
    if cnt == k:
        print(i)
        break
else:
    print(-1)
