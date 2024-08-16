import sys
sys.stdin = open('C:/Users/SSAFY/Desktop/깃/SSAFY_Algorithm/SWEA/SWEA_11315_오목/sample_input.txt', 'r')

def check(matrix, N):
    for r in range(N):
        for c in range(N):
            if matrix[r][c] == 'o':
                for k in range(4):
                    for m in range(1, 5):
                        dr = r + m * r_delta[k]
                        dc = c + m * c_delta[k]
                        if (0 <= dr < N) and (0 <= dc < N):
                            if matrix[dr][dc] != 'o':
                                break
                        # 인덱스가 넘어갔을 때 확실히 멈춰줘야 제대로 동작함
                        else: break
                    else:
                        return 'YES'
    return 'NO'

T = int(input())

r_delta = [0, 1, 1, 1]
c_delta = [1, 0, 1, -1]

for tc in range(1, T + 1):
    N = int(input())
    board = [list(input()) for _ in range(N)]
    ans = check(board, N)
    
    print(f'#{tc} {ans}')