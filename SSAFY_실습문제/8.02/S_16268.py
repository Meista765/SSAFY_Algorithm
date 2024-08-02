import sys
sys.stdin = open('input.txt','r')
T = int(input())

dr = [-1,1,0,0] # 상하좌우
dc = [0,0,-1,1]

for test_case in range(1,T+1):
    N, M = map(int, input().split())
    arr = [[0] * (M+2)] + [[0] + list(map(int,input().split())) + [0] for _ in range(N)] + [[0] * (M+2)]


    max_cnt = 0

    for i in range(1,N+1):
        for j in range(1,M+1):
            cnt = arr[i][j]          # 풍선 갯수
            for k in range(4):

                cnt += arr[i+dr[k]][j+dc[k]]

            if max_cnt < cnt:
                max_cnt = cnt

    print(f'#{test_case} {max_cnt}')
  #