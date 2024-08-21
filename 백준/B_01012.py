import sys
sys.stdin = open('input.txt')
from collections import deque

def BFS(s):
    global cnt
    cnt += 1    # BFS 함수가 호출될 때 cnt +1
    q = deque()
    q.append(s)
    visited[s[0]][s[1]] = 1  # q에 append 하면서 방문 리스트에 체크
    # 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while q: # q가 빌 때까지
        v = q.popleft()
        for k in range(4):
            nr = v[0] + dr[k]
            nc = v[1] + dc[k]

            if 0 <= nr < N and 0 <= nc < M and maze[nr][nc] == 1 and visited[nr][nc] != 1: # 인덱스를 벗어나지 않고
                q.append((nr,nc))                                                      # 해당 지점에 배추가 있고 방문하지 않은 곳이면
                visited[nr][nc] = 1


T = int(input())

for test_case in range(1,T+1):
    M, N, K = map(int,input().split())  # M: 열의 길이 N: 행의 길이, K: 배추의 수
    maze = [[0]*M for _ in range(N)]    # 배추 밭
    visited = [[0]*M for _ in range(N)] # 방문리스트
    cnt = 0     # 지렁이 수 => 결과
    # 배추심기
    for _ in range(K):
        c,r = map(int,input().split()) # x,y 좌표 식으로 주기 때문에 헷갈리지 않게 주의!!!!
        maze[r][c] = 1

    for i in range(N):              # 배추 밭을 순회
        for j in range(M):
            if maze[i][j] == 1 and visited[i][j] == 0: # 배추 밭을 순회 하면서 배추가 있고 방문하지 않은 곳이면 BFS호출
                BFS((i,j))

    print(cnt)


