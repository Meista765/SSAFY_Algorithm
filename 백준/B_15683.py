# import sys
# sys.stdin = open('input.txt')
'''
아이디어: DFS(백트래킹) + 구현
1. cctv의 종류 및 위치를 저장
2. 재귀함수를 돌면서 리스트(pick)에 어떤 방향으로 탐색을 진행할 것인지 저장
3. 재귀호출 마지막에 위의 리스트에서 저장한 탐색방향으로 각각의 cctv를 탐색하면서 visited 배열에 감시 구역을 체크
4.visited 배열에서 감시 구역이 아닌 부분의 갯수를 세준다.
'''

def check():
    visited = [[0] * M for _ in range(N)]

    for i in range(cnt):
        for k in pick[i]:
            nr = cctv[i][0]
            nc = cctv[i][1]
            while True:
                nr = nr + dr[k]
                nc = nc + dc[k]
                if nr < 0 or nr >= N or nc < 0 or nc >= M or arr[nr][nc] == 6:
                    break
                elif arr[nr][nc] == 0:
                    visited[nr][nc] = '#'

    count = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0 and arr[i][j] == 0:
                count += 1

    return count


def dfs(n):
    global min_val

    # 종료조건
    if n == cnt:
        count = check()
        min_val = min(min_val, count)
        return

    t = cctv[n][2]

    for direction in cctv_direction[t]:
        pick.append(direction)
        dfs(n+1)
        pick.pop()


N, M = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 방향설정: 상우하좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


# cctv 갯수와 종류 파악
cctv = []
cnt = 0
for i in range(N):
    for j in range(M):
        if 0 < arr[i][j] < 6:
            cctv.append((i,j,arr[i][j]))
            cnt += 1

cctv_direction = {
    1: [[0], [1], [2], [3]],                            # 상, 우, 하, 좌
    2: [[0, 2], [1, 3]],                                # (상,하), (우,좌)
    3: [[0, 1], [1, 2], [2, 3], [0, 3]],                # (상,우), (우,하), (하,좌), (좌,상)
    4: [[0, 1, 3], [0, 1, 2], [1, 2, 3], [0, 2, 3]],    # (상,우,좌), (상,우,하), (우,하,좌), (상,하,좌)
    5: [[0, 1, 2, 3]]                                    # (상우하좌)
}


min_val = N * M
pick = []
# print(cctv)
# print(cnt)
# print(cctv_direction[1])
# print(cctv[0][0],cctv[0][1])
dfs(0)
print(min_val)


