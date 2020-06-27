import sys
sys.stdin = open("input.txt", "rt")

string = input()

def cntPrime(x):
    res = 0
    for i in range(1,x+1): 
        if x % i == 0:
            res += 1
    return res

number = 0 
for char in string:
    if char.isdigit():
        digit = int(char)
        number = (number * 10) + digit
print(number)
print(cntPrime(number))