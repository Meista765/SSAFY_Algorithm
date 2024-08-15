import sys
sys.stdin = open('input.txt')
T = int(input())

for test_case in range(1,T+1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    max_sum = float('-inf')
    # for i in range(N):
    #     for j in range(N):
    #         cnt = 0
    #         for k in range(M):
    #             for l in range(M):
    #                 if 0 <= i+k < N and 0 <= j+l < N:
    #                     cnt += arr[i+k][j+l]
    #         if max_sum < cnt:
    #             max_sum = cnt
    # print(f'#{test_case} {max_sum}')
    # =====================================================================
    # 다른
    for i in range(N-M-1):
        for j in range(N-M-1):
            cnt = 0
            for k in range(M):
                for l in range(M):
                    cnt += arr[i+k][j+l]
            if max_sum < cnt:
                max_sum = cnt
    print(f'#{test_case} {max_sum}')
