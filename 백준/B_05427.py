'''
1. 불을 먼저 지른
2. 상근이가 이동하는 곳이 불이 번진 시간보다 작으면 이동 가능

========================================================
'.': 빈 공간
'#': 벽
'@': 상근이의 시작 위치
'*': 불
'''

from collections import deque


# 불의 위치 찾기
def find_fire():
    fire_q = deque()
    for i in range(h):
        for j in range(w):
            if building[i][j] == '*':
                fire_q.append((i,j))
    return fire_q

# 상근이 위치찾기
def find_person():
    for i in range(h):
        for j in range(w):
            if building[i][j] == '@':
                return (i,j)

# 불지르기
def BFS_1():
    global fire_q
    time = 0
    # 상하좌우
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    while fire_q:  # 큐가 빌 때까지
        v = fire_q.popleft()
        building[v[0]][v[1]] = time
        time += 1
        for k in range(4):
            nr = v[0] + dr[k]
            nc = v[1] + dc[k]
            # 빈공간이거나 상근이 처음 자리이면 불지르기
            if 0 <= nr < h and 0 <= nc < w and (building[nr][nc] == '.' or building[nr][nc] == '@'):
                building[nr][nc] = time
                fire_q.append((nr,nc))

# 상근이 탈출
def BFS_2(s):
    q = deque()
    q.append(s)
    building[s[0]][s[1]] = 0  # 상근이 처음 자리 0으로 세팅
    # 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while q:    # q가 빌때까지
        v = q.popleft()
        if v[0] == 0 or v[0] == h-1 or v[1] == 0 or v[1] == w-1:    # 탈출 직전이면
            return building[v[0]][v[1]] + 1


        for k in range(4):
            nr = v[0] + dr[k]
            nc = v[1] + dc[k]
            if 0 <= nr < h and 0 <= nc < w and building[nr][nc] != '#' and  building[v[0]][v[1]]+1 < building[nr][nc]:
                building[nr][nc] = building[v[0]][v[1]]+1
                q.append((nr,nc))
    return 'IMPOSSIBLE'


T = int(input())
for test_case in range(1,T+1):
    w, h = map(int,input().split()) # w: 너비 h: 높이
    building = [list(input()) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    fire_q = find_fire()
    s = find_person()
    BFS_1()   # 불지르기 함수 호출
    result = BFS_2(s)   # 상근이 탈출
    print(result)











