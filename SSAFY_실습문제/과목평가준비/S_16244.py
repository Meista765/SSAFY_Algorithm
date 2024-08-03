import sys
sys.stdin = open('input.txt','r')

T = int(input())



for test_case in range(1,T+1):

    r,c,N = map(int,input().split())
    arr = [[0]*10 for _ in range(10)]
    
    # 우, 하, 좌, 상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    for i in range(4):
        for _ in range(N-1):
            r = r+dr[i]
            c = c+dc[i]

            arr[r][c] = 1
    print(f'#{test_case}') 
    for j in range(10):
        print(*arr[j])
        

