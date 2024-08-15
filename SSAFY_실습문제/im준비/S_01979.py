T = int(input())

for test_case in range(1,T+1):
    N, K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    answer = 0
    # 가로 탐색
    for i in range(N):
        cnt = 0
        for j in range(N-K+1):
            if arr[i][j] == 1:
                cnt += 1
            elif arr[i][j] == 0 and j:
                if cnt == K:
                    answer += 1
                cnt = 0




