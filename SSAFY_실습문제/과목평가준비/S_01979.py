import sys
sys.stdin = open('input.txt','r')
T = int(input())

for test_case in range(1,T+1):
    
    N, K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)] # 0은 채워진 칸 1은 빈칸

    cnt = 0 # 가능한 경우의 수
    # 행탐색  
    for i in range(N):
        one_cnt = 0 
        for j in range(N):
            if arr[i][j] == 1:   # arr[i][j]가 1이면 갯수를 세어준다.
                one_cnt += 1
            else:                # arr[i][j]가 0이면 이전까지 1의 갯수가 K랑 같은지 확인한다.
                if one_cnt == K: # 만약 K랑 같다면 cnt +1을 해준다.
                    cnt += 1

                one_cnt = 0
        if one_cnt == K:
            cnt += 1

    # 열 탐색

    for j in range(N):
        one_cnt = 0
        for i in range(N):
            if arr[i][j] == 1:
                one_cnt += 1
            else:
                if one_cnt == K:
                    cnt +=1
                
                one_cnt = 0
        if one_cnt == K:
            cnt += 1
    print(f'#{test_case} {cnt}')

