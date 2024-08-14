from collections import deque
import sys
sys.stdin = open('input.txt')


# 출발 지점: 2, 도착 지점: 3, 0: 통로, 1: 벽

# 출발 지점 찾기
def find_start():
    for y in range(16):
        for x in range(16):
            if maze[y][x] == 2:
                return (y,x)


# bfs 함수
def bfs(s):
    q = deque()
    q.append(s)
    visited[s[1]][s[0]] = 1
    # 상하좌우
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    while q:
        v = q.popleft()
        if maze[v[1]][v[0]] == 3:
            return 1
        for k in range(4):
            nx = v[0] + dx[k]
            ny = v[1] + dy[k]

            if 0 <= nx < 16 and 0 <= ny < 16 and maze[ny][nx] != 1 and visited[ny][nx] == 0:
                q.append((ny,nx))
                visited[ny][nx] = 1
    return 0



for test_case in range(1,11):

    tc = int(input())
    maze = [list(map(int,input())) for _ in range(16)]
    start = find_start()
    visited = [[0] * 16 for _ in range(16)]

    result = bfs(start)
    print(f'#{test_case} {result}')
