from collections import deque

# 현재 먹을 수 있는 먹이의 위치 찾기
def bfs(start):
    q = deque()
    q.append(start)
    visited = [[0] * N for _ in range(N)]
    visited[start[0]][start[1]] = 1         # 현재 아기상어의 위치 방문체크

    while q:
        v = q.popleft()
        for k in range(4):
            nr = v[0] + dr[k]
            nc = v[1] + dc[k]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
                if cur_size >= arr[nr][nc]:
                    q.append((nr,nc))
                    visited[nr][nc] = visited[v[0]][v[1]] + 1
    return visited

# 아기 상어의 현재 위치 찾기
def find_shark():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 9:
                arr[i][j] = 0
                return (i,j)

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
start = find_shark()
cur_size = 2            # 아기 상어의 현재 크기
cnt = 0                 # 현재 사이즈에서 먹은 물고기 수
time = 0                # 타이머
# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

while True:
    visitied = bfs(start)
    min_distance = float('inf')
    for i in range(N):
        for j in range(N):
            # 먹을 수 있는 크기이면서 거리가 최소인 곳으로 이동(위에서부터 아래로 왼쪽에서부터 오른쪽으로 순회하니까 우선순위는 지켜짐)
            if arr[i][j] != 0 and arr[i][j] < cur_size and visitied[i][j] != 0 and visitied[i][j] < min_distance:
                min_distance = visitied[i][j]
                start = (i,j)
    # 최소값이 갱신되지 않는다면
    if min_distance == float('inf'):
        break
    arr[start[0]][start[1]] = 0
    cnt += 1
    time += visitied[start[0]][start[1]] -1
    # 현재크기에서 먹은 물고기의 수가 현재 크기랑 같다면 현재사이즈 +1하고 먹은 물고기의 수 0으로 초기화
    if cnt == cur_size:
        cur_size += 1
        cnt = 0

print(time)