import sys
sys.stdin = open("input.txt", "rt")

N = int(input())
arr = list(map(int, input().split()))

avg = round((sum(arr) / N) + 0.5)

min = 2147000000
for (idx, x) in enumerate(arr):
    tmp=abs(x-avg)
    if tmp < min:
        min = tmp
        score = x
        res = idx + 1
    elif tmp == min:
        if x > score:
            score = x
            res = idx + 1
print(avg, res)

# enumerate
# pyhton에서 round는 round_haf_even방식을 사용해서 반올림에 사용하면 안됨.
# 따라서 0.5를 더해서 round
# abs
