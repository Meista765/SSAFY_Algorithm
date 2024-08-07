import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1,T+1):

    N,M = map(int,input().split())
    arr = list(map(int,input().split()))
    
    i = [0] * M
    j = [0] * M

    for k in range(M):
        i[k], j[k] = map(int,input().split())
    
    for k in range(M):
        for l in range(i[k],i[k]+j[k]-1):
            if l < N:
                arr[l] = arr[i[k]-1]
    print(f'#{test_case}', end = ' ')
    print(*arr)

    