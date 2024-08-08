
def dfs(start):
    global end
    stack = [start]

    # 상하좌우
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]

    while stack:            # stack이 비어있지 않을 때까지
        r, c = stack.pop()  # 현재 위치

        if maze[r][c] == 3: # 현재 위치가 목표지점이면 끝
            return 1
        else:
            visited[r][c] =1    # 방문리스트 체크
            # 상하좌우 체크하면서 탐색 시작
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if 0<= nr <N and 0<= nc < N and maze[nr][nc] != 1 and visited[nr][nc] == 0:   #범위를 벗어나지 않고 방문하지 않은 위치이면
                    stack.append((nr,nc))



    return 0


T = int(input())
for test_case in range(1,T+1):
    N= int(input())

    maze = [list(map(int,input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]             # 방문 안했으면 0 했으면 1

    # 시작점 찾기
    for j in range(N):
        if maze[N-1][j] == 2:
            start = (N-1, j)

    # 도착지점 찾기
    for j in range(N):
        if maze[0][j] == 3:
            end = (0, j)

    result = dfs(start)
    print(f'#{test_case} {result}')



