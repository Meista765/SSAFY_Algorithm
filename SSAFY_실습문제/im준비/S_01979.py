import sys
sys.stdin = open('input.txt')
T = int(input())

for test_case in range(1,T+1):
    N, K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    answer = 0
    # 가로 탐색
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 1:
                cnt += 1
            else:
                if cnt == K:
                    answer += 1

                cnt = 0
        # 마지막이 1로 끝났을 경우를 위해 한번 더 비교
        if cnt == K:
            answer += 1


    # 열 탐색
    for j in range(N):
        cnt = 0
        for i in range(N):
            if arr[i][j] == 1:
                cnt += 1
            else:
                if cnt == K:
                    answer +=1
                cnt = 0
        # 마지막이 1로 끝났을 경우를 위해 한번 더 비교
        if cnt == K:
            answer += 1


    print(f'#{test_case} {answer}')




