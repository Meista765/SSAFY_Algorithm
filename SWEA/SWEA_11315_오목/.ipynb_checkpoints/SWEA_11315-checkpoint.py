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
                    else:
                        return 'YES'
    return 'NO'

                            
T = int(input())

r_delta = [1, 0, 1, 1]
c_deta = [1, 0, 1, -1]

for tc in range(1, T + 1):
    N = int(input())
    board = [list(input()) for _ in range(N)]
    ans = check(matrix, N)
    
    print(f'#{tc} {ans}')