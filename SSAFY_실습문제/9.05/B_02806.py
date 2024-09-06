import sys
sys.stdin = open('input.txt')

def check(cols,r,c):
    for i in range(r):
        if (r - i) == abs(cols[i] - c):
            return True
    return False


def nqueen(k):      # k -> 행의 좌표 and queen의 갯수
    global cnt

    if k == N:
        cnt += 1

    else:
        for i in range(N):
            if visited[i] or check(cols,k,i):
                continue
            visited[i] = 1
            cols[k] = i
            nqueen(k+1)
            visited[i] = 0


T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    visited = [0] * N       # 같은 열에 있는 지 확인
    cols = [0] * N          # 열 좌표 확인(대각선 방향 확인할 때 사용할 것)
    cnt = 0                 # 가능한 경우의 수
    nqueen(0)
    print(f'#{test_case} {cnt}')

