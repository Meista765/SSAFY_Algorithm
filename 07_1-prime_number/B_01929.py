# 소수 구하기
import sys
#input = sys.stdin.readline
sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")

M, N = map(int, input().split())    # M <= 소수 <= N

arr = [0] * (N+1)
arr[1] = 1
for i in range(2, N+1):
    for j in range(i, N+1, i):
        if j != i:
            arr[j] = 1

for i in range(M, N+1):
    if arr[i] == 0:
        print(i)