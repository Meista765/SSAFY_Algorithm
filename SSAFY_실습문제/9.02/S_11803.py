import sys
sys.stdin = open('input.txt')

def back_track(v,cnt,s):    # v: 방문 위치, cnt = 방문 횟수, s = 현재까지의 합
    global min_val
    # 가지치기
    if s > min_val:
        return
    if cnt == N-1:          # 1은 무조건 맨 마지막에 방문
        if min_val > s+arr[v][0]:
            min_val = s+arr[v][0]

    else:
        for i in range(1,N):
            if v == i:      # 자기 자신 제외
                continue
            if not visited[i]:  # 방문하지 않은 곳이면
                visited[i] = 1
                back_track(i,cnt+1,s+arr[v][i])
                visited[i] = 0


T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [0] * N       # 방문 체크를 위한 리스트
    min_val = 100 * N       # 초기 최솟값
    back_track(0,0,0)
    print(f'#{test_case} {min_val}')

