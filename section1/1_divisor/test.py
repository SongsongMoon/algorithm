import sys
sys.stdin = open("in5.txt", "rt")

inputNumber = input()

T, N, s, e, k = map(int, inputNumber.split())
print(T,N,s,e,k)