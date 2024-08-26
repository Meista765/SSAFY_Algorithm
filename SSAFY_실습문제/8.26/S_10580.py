import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1,T+1):
    N = int(input())     # 전선의 수
    line = [list(map(int,input().split())) for _ in range(N)]   # 전깃줄
    line.sort()

    cnt = 0     # 접점의 갯수
    for i in range(1,N):    # i: 1 ~ N
        for j in range(i):  # j: 0 ~ i-1
            if line[i][1] < line[j][1]:
                cnt += 1

    print(f'#{test_case} {cnt}')

