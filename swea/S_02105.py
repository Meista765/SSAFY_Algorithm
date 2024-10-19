import sys
sys.stdin = open('S_02105.txt')

# i: 시작 행 좌표, j: 시작 점 열 좌표, []: 지나오면서 들린 디저트 카페, way: 진행방향 표시 0: 우하, 1: 좌하, 2: 좌상, 3:우상
def dfs(sr, sc, path, way):
    global max_cnt

    # 종료 조건 -> 시작점에 되돌아 왔을 때
    if sr == i and sc == j and len(path) >= 4:
        max_cnt = max(len(path), max_cnt)
        return

    if way < 3:
        d = 2
    else:
        d = 1

    for k in range(way, way+d):         # 직진 or 꺾기
        nr = sr + dr[k]
        nc = sc + dc[k]
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] not in path:      # 인덱스 안 벗어나고 # 지금까지 들린 디저트 가게와 겹치지 않으면
            path.append(arr[nr][nc])
            dfs(nr, nc, path, k)
            path.pop()


T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    # path = []               # 가는 길에 들렸던 디저트 카페 저장

    # 시계 방향: 우하, 좌하, 좌상, 우상
    dr = [1, 1, -1, -1]
    dc = [1, -1, -1, 1]

    max_cnt = -1
    for i in range(N):
        for j in range(N):
            dfs(i, j, [], 0)
    print(f'#{test_case} {max_cnt}')