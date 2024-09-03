import sys
sys.stdin = open('./sample_input.txt', 'r')

def check(sr, sc, length):
    for r in range(sr, sr + length):
        for c in range(sc, sc + length):
            if matrix[r][c] != '#':
                return 'no'
    else:
        return 'yes'
    

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(input()) for _ in range(N)]

    for r in range(N):
        length = 0
        for c in range(N):
            # 칼럼 끝나는 부분 잘 선택하면 된다
            if matrix[r][c] == '#':
                sr, ec = r, c
                length += 1
        if length > 0:
            break
    
    ans = check(sr, ec - length + 1, length)

    print(f'#{tc} {ans}')