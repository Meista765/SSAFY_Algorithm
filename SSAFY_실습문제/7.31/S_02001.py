import sys
sys.stdin = open('input.txt','r')

T = int(input())

for test_case in range(1,T+1):

    N, M = map(int,input().split())

    matrix = [list(map(int,input().split())) for _ in range(N)]
    max_val = 0  # 죽인 파리 수 최대값
    for i in range(0,N-M+1):
        for j in range(0,N-M+1):
            s = 0

            for k in range(M): # 이동하면서 죽인 파리 수 더하기
                for l in range(M):
                    s += matrix[i+k][j+l]


            if max_val < s:
                max_val = s


    print(f'#{test_case} {max_val}')

