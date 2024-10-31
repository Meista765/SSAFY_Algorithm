# 로봇
import sys
from collections import deque
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
#sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")
#input = sys.stdin.readline

# 입력 받기
ROW, COL = map(int, input().split())  # 행, 열
arr = [list(map(int, input().split())) for _ in range(ROW)]  # 배열
start_row, start_col, start_dir = map(int, input().split())  # 시작 지점 행, 열, 방향
end_row, end_col, end_dir = map(int, input().split())  # 도착 지점 행, 열, 방향

# 문제에서 주어진 방향을 프로그램에서 쉽게 사용하도록 변환
RIGHT, LEFT, DOWN, UP = 1, 2, 3, 4
direction_map = {UP: 0, RIGHT: 1, DOWN: 2, LEFT: 3}
start_dir = direction_map[start_dir]
end_dir = direction_map[end_dir]

# 배열 좌표는 (0, 0) 기준으로 설정
start_row -= 1
start_col -= 1
end_row -= 1
end_col -= 1

# 방향 이동 (상, 우, 하, 좌)
DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# 방문 배열 (행, 열, 방향 별로 최소 명령 횟수를 기록)
visited = [[[float('inf')] * 4 for _ in range(COL)] for _ in range(ROW)]
queue = deque([(start_row, start_col, start_dir, 0)])  # (행, 열, 방향, 명령횟수)
visited[start_row][start_col][start_dir] = 0

while queue:
    r, c, cur_dir, count = queue.popleft()

    # 도착 지점과 방향에 도달한 경우 최소 명령 횟수 갱신
    if (r, c, cur_dir) == (end_row, end_col, end_dir):
        print(count)
        break

    # 전진 명령 (1~3칸)
    for n in range(1, 4):
        nr, nc = r + DIR[cur_dir][0] * n, c + DIR[cur_dir][1] * n
        if 0 <= nr < ROW and 0 <= nc < COL and arr[nr][nc] == 0:
            if visited[nr][nc][cur_dir] > count + 1:
                visited[nr][nc][cur_dir] = count + 1
                queue.append((nr, nc, cur_dir, count + 1))
        else:
            break  # 전진 불가능하면 정지

    # 방향 전환 명령 (왼쪽 또는 오른쪽으로 90도 회전)
    for turn in [-1, 1]:  # -1은 왼쪽, 1은 오른쪽 회전
        new_dir = (cur_dir + turn) % 4
        if visited[r][c][new_dir] > count + 1:
            visited[r][c][new_dir] = count + 1
            queue.append((r, c, new_dir, count + 1))