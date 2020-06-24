import sys
sys.stdin = open("input.txt", "rt")

cntCase = int(input())
res = 0
for i in range(cntCase):
    tmp = input().split()
    tmp.sort()
    a, b, c = map(int, tmp)

    if a == b and b == c:
        money = 10000 + (a * 1000)
    elif a == b or a == c:
        money = 1000 + (a * 100)
    elif b == c:
        money = 1000 + (b * 100)
    else:
        money = c * 100

    if res < money:
        res = money
print(res)
    


"""
1 1 3
1 3 1
3 1 1

a == c
a == c
"""
