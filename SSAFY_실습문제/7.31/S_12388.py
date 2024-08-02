import sys
sys.stdin = open('input.txt', 'r')
T = int(input())



for test_case in range(1,T+1):

    # 10 x 10 크기의 matrix를 만들고 안에 다 0을 채운다
    matrix = [[0] * 10 for _ in range(10)]

    N = int(input()) # 칠할 영역의 개수
    cnt = 0 #  보라색 수
    for _ in range(N):

        r1,c1,r2,c2,color = map(int,input().split())

        for i in range(r1,r2+1): # 2,3,4
            for j in range(c1,c2+1): # 2, 3, 4
                matrix[i][j] += color
                if matrix[i][j] == 3:
                    cnt += 1
    print(f'#{test_case} {cnt}')


