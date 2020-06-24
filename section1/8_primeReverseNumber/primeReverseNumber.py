import sys
sys.stdin = open("input.txt", "rt")

cntArr = int(input())
arr = list(map(int, input().split()))

def isPrime(x):
    for i in range(2,x):
        if x % i == 0:
            return False
    else:
        return True
    
# 12345 -> 54321
"""
1. 12345
    r = 5
    reversed = 5
    x = 1234
2. 1234
    r = 4
    reversed = 50 + 4
    x = 123
3. 123
    r = 3
    reversed = 540 + 3
    x = 12
4. 12
    r = 2
    reversed = 5430 + 2
    x = 1
5. 1
    r = 1
    reversed = 54320 + 1
    x = 0
"""
def reverse(x):
    reversed = 0
    while(x!=0):
        r = int(x%10)
        reversed = reversed*10 + r
        x = int(x/10)
    return reversed

for element in arr:
    rev = reverse(element)
    if isPrime(rev):
        print(rev)