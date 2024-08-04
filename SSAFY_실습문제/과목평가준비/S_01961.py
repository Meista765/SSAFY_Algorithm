# import sys
# sys.stdin = open('input.txt','r')

T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    # 90도 회전 

    arr_90 = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr_90[j][N-1-i] =arr[i][j]

    # 180도 회전

    arr_180 = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr_180[j][N-1-i] = arr_90[i][j]

    # 270도 회전 

    arr_270 = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr_270[j][N-1-i] = arr_180[i][j]

    print(f'#{test_case}')
    
    for i in range(N):
        for a in range(N):
            print(arr_90[i][a],end='')
        print(' ',end='')
        for b in range(N):
            print(arr_180[i][b], end='')
        print(' ', end='')
        for c in range(N):
            print(arr_270[i][c], end='')
        print()
        
