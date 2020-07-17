import sys
sys.stdin = open("input.txt", "rt")
s = input()
stack = []
cnt = 0

for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])
    else:
        if s[i-1] == '(':
            stack.pop()
            cnt += len(stack)
        else:
            stack.pop()
            cnt += 1

print(cnt)