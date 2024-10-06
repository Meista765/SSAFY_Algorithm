import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    Q = int(input())

    for _ in range(Q):
        C, command = input().split()
        C = int(C)
        for i in range(C):
            if command[i] == 'R':

