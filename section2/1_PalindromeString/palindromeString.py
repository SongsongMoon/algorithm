import sys
sys.stdin = open("input.txt","rt")

def isPalindrome(s): 
    return s == s[::-1]

cntCase = int(input())

for i in range(cntCase):
    string = input()
    lenStr = len(string)

    for idx in range(lenStr//2):
        if string[idx].lower() != string[lenStr-1-idx].lower():
            print("#%d NO" %(i+1))
            break
    else:
        print("#%d YES" %(i+1))

# array[::-1] --> reversed
# print("%d" %i)
# len()
# // 나눈 후 소수점 이하 버림