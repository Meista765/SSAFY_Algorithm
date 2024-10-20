import sys
sys.stdin = open('sample_input.txt', 'r')

# direction: 현재 진행 방향, count: 디저트 먹은 수, eaten: 먹은 디저트 종류, turn_count: 방향 전환 수
def dfs(r, c, start_r, start_c, direction, count, eaten, turn_count):
    global max_count
    # 사각형이 완성되었고, 시작 지점에 다다르면 업데이트 후 종료
    if turn_count == 3 and r == start_r and c == start_c:
        max_count = max(max_count, count)
        return
    # 시작 지점을 찾지 못하고 계속 탐색하다가 방향이 전환되면 즉시 종료
    if turn_count == 4:
        return
    
    # 현재 진행 방향 그대로 가거나 방향 전환하기
    ## => 지금 방향 그대로 dfs or 방향을 바꾼 뒤 dfs
    for i in range(2):  
        new_direction = (direction + i) % 4
        nr = r + dr[new_direction]
        nc = c + dc[new_direction]

        # 이동 가능하고, 아직 안 먹은 종류면 탐색
        if 0 <= nr < N and 0 <= nc < N and field[nr][nc] not in eaten:
            eaten.add(field[nr][nc])
            # 새로운 좌표로 이동 후 계속 탐색
            ## 일단 이동은 했으니 먹은 횟수와 종류는 기록//방향을 바꾸었는지, 아닌지에 따라 방향 전환 수 추가
            dfs(nr, nc, start_r, start_c, new_direction, count + 1, eaten, turn_count + (i == 1))
            # 다시 돌아올 때 디저트 제거
            eaten.remove(field[nr][nc])

for tc in range(1, int(input()) + 1):
    N = int(input())
    field = [list(map(int, input().split())) for _ in range(N)]
    dr = [-1, -1, 1, 1]
    dc = [1, -1, -1, 1]
    max_count = -1

    for r in range(N):
        for c in range(N):
            dfs(r, c, r, c, 0, 0, set([field[r][c]]), 0)

    print(f'#{tc} {max_count}')
