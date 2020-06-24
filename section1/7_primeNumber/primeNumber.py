import sys
sys.stdin = open("input.txt", "rt")

inputNumber = int(input())

def isPrime(x):
    cnt = 0
    for i in range(1,x+1):
        if x % i == 0:
            cnt += 1
    if cnt == 2:
        return True
    else:
        return False

def isPrime2(x):
    for i in range(2,x):
        if x % i == 0:
            return False
    else:
        return True

res = 0
for i in range(2,inputNumber+1):
    if isPrime2(i):
        res += 1

print(res)