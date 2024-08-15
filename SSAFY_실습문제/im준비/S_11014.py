import sys
sys.stdin = open('input.txt')
T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    # 1번: 행: 0 ~ i-1 열: 0 ~ j-1
    # 2번: 행: 1번 ~ N  열: 행 0 ~ j-1
    # 3번: 행: 0 ~ N  열: i ~ N
    min_diff = float('inf')
    for i in range(1,N):        # 1 ~ N-1
        for j in range(1,N):    # 1 ~ N-1

            area_1 = area_2 = area_3 = 0
            # area_1의 수확량
            for r in range(i):
                for c in range(j):
                    area_1 += arr[r][c]

            # area_2의 수확량
            for r in range(i,N):
                for c in range(j):
                    area_2 += arr[r][c]

            # area_3의 수확량
            for r in range(0,N):
                for c in range(j,N):
                    area_3 += arr[r][c]

            # 최대값 및 최소값
            max_val = max(area_1,area_2,area_3)
            min_val = min(area_1,area_2,area_3)
            diff = max_val - min_val

            min_diff = min(min_diff,diff)
    print(f'#{test_case} {min_diff}')





