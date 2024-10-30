# # 로봇
# import sys
# from collections import deque
# #sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
# sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")
# #input = sys.stdin.readline

# DEBUG = 0


# def change_dir(goal_dir, cur_dir):
#   if goal_dir == cur_dir:   # 같은 방향
#     return 0
#   elif abs(goal_dir - cur_dir) == 2:    # 동-서, 남-북
#     return 2
#   else:
#     return 1


# def BFS(start_row, start_col, start_dir):   # 행, 열, 방향, 명령 횟수
#   global visited, MIN_COMMAND_CNT
  
#   queue = deque()
#   queue.append((start_row, start_col, start_dir))
  
#   while queue:
#     r, c, cur_dir = queue.popleft()
    
#     # 종료 조건: 도착 지점에 도달하면 종료
#     if (r, c) == (end_row, end_col):
#       visited[r][c] += change_dir(end_dir, cur_dir)
#       MIN_COMMAND_CNT = min(visited[r][c], MIN_COMMAND_CNT)
#       continue
      
#     # 가지 치기: 현재 명령 횟수가 지금까지 나온 최소 명령 횟수보다 크거나 같은 경우
#     if visited[r][c] >= MIN_COMMAND_CNT:
#       continue
    
#     # 사방 확인 후 갈 수 있는 곳으로 가기
#     for goal_dir in range(4):
#       for n in range(1, 4):
#         nr, nc = r + DIR[goal_dir][0]*n, c + DIR[goal_dir][1]*n
#         if 0 <= nr < ROW and 0 <= nc < COL and not arr[nr][nc] and not visited[nr][nc]:
#           command_cnt = visited[r][c]
#           # 방향 변경 몇 번 해야하는지 구해서 명령 횟수에 더하기
#           command_cnt += change_dir(goal_dir, cur_dir)
#           # 앞으로 한 칸 갔으니까 +1
#           command_cnt += 1
          
#           visited[nr][nc] += command_cnt
#           queue.append((nr, nc, goal_dir))
      
#           if DEBUG:
#             print(goal_dir, cur_dir, change_dir(goal_dir, cur_dir))
#             print(nr, nc)
#             print(command_cnt)
#             for i in range(ROW):
#               print(*visited[i])
#             print()
#         else:
#           break
      
        
# # 입력 받기
# ROW, COL = map(int, input().split())    # 행, 열
# arr = [list(map(int, input().split())) for _ in range(ROW)]   # 배열
# start_row, start_col, start_dir = map(int, input().split())   # 시작 지점 행, 열, 방향
# end_row, end_col, end_dir = map(int, input().split())         # 도착 지점 행, 열, 방향

# # 내가 정한 방향 숫자로 바꿔주기
# RIGHT, LEFT, DOWN, UP = 1, 2, 3, 4    # 문제에서 정한 방향 숫자
# my_dir_dict = {UP:0, RIGHT:1, DOWN:2, LEFT:3}   # 내가 정한 방향 숫자 (시계방향)
# start_dir = my_dir_dict[start_dir]; end_dir = my_dir_dict[end_dir]

# # 문제에서는 (1, 1)이 배열 좌측 최상단이지만, 계산의 편의를 위해 (0, 0)으로 바꿔주기
# start_row -= 1; start_col -= 1
# end_row -= 1; end_col -= 1

# if DEBUG:
#   print('시작:', (start_row, start_col), start_dir)
#   print('도착:', (end_row, end_col), end_dir)

# # 풀이에 필요한 글로벌 변수들
# DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]    # 상 -> 우 -> 하 -> 좌
# visited = [[0] * COL for _ in range(ROW)]   # 방문 배열
# visited[start_row][start_col] = 1           # 시작 지점 방문 표시
# MIN_COMMAND_CNT = float('inf')              # 지금까지 나온 최소 명령 횟수

# # DFS로 도착 지점에 도달하기 위한 최소 명령 횟수 찾기
# BFS(start_row, start_col, start_dir)

# # 시작 지점 방문 표시했던 1 빼주기
# print(MIN_COMMAND_CNT - 1)

import sys
from collections import deque
#sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")
#input = sys.stdin.readline

DEBUG = 0

def change_dir(goal_dir, cur_dir):
    if goal_dir == cur_dir:
        return 0
    elif abs(goal_dir - cur_dir) == 2:  # 동-서, 남-북
        return 2
    else:
        return 1

def BFS(start_row, start_col, start_dir):
    global visited, MIN_COMMAND_CNT
    
    queue = deque()
    queue.append((start_row, start_col, start_dir, 0))  # (행, 열, 방향, 명령 횟수)
    visited[start_row][start_col][start_dir] = 0
    
    while queue:
        r, c, cur_dir, command_cnt = queue.popleft()
        
        # 종료 조건: 도착 지점에 도달하면 종료
        if (r, c) == (end_row, end_col) and cur_dir == end_dir:
            MIN_COMMAND_CNT = min(command_cnt, MIN_COMMAND_CNT)
            continue

        # 가지 치기: 현재 명령 횟수가 지금까지 나온 최소 명령 횟수보다 크거나 같은 경우
        if command_cnt >= MIN_COMMAND_CNT:
            continue

        # 사방 확인 후 갈 수 있는 곳으로 가기
        for goal_dir in range(4):
            # 방향 전환 횟수 추가
            new_command_cnt = command_cnt + change_dir(goal_dir, cur_dir)
            
            for n in range(1, 4):
                nr, nc = r + DIR[goal_dir][0] * n, c + DIR[goal_dir][1] * n
                if 0 <= nr < ROW and 0 <= nc < COL and not arr[nr][nc]:
                    if new_command_cnt + 1 < visited[nr][nc][goal_dir]:
                        visited[nr][nc][goal_dir] = new_command_cnt + 1
                        queue.append((nr, nc, goal_dir, new_command_cnt + 1))
                    
                    if DEBUG:
                        print(goal_dir, cur_dir, change_dir(goal_dir, cur_dir))
                        print(nr, nc)
                        print(new_command_cnt + 1)
                        for i in range(ROW):
                            print(*[min(v) for v in visited[i]])
                        print()
                else:
                    break

# 입력 받기
ROW, COL = map(int, input().split())  # 행, 열
arr = [list(map(int, input().split())) for _ in range(ROW)]  # 배열
start_row, start_col, start_dir = map(int, input().split())  # 시작 지점 행, 열, 방향
end_row, end_col, end_dir = map(int, input().split())  # 도착 지점 행, 열, 방향

# 내가 정한 방향 숫자로 바꿔주기
RIGHT, LEFT, DOWN, UP = 1, 2, 3, 4  # 문제에서 정한 방향 숫자
my_dir_dict = {UP: 0, RIGHT: 1, DOWN: 2, LEFT: 3}  # 내가 정한 방향 숫자 (시계방향)
start_dir = my_dir_dict[start_dir]
end_dir = my_dir_dict[end_dir]

# 문제에서는 (1, 1)이 배열 좌측 최상단이지만, 계산의 편의를 위해 (0, 0)으로 바꿔주기
start_row -= 1
start_col -= 1
end_row -= 1
end_col -= 1

# 풀이에 필요한 글로벌 변수들
DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 상 -> 우 -> 하 -> 좌
visited = [[[float('inf')] * 4 for _ in range(COL)] for _ in range(ROW)]  # 방향 별 최소 방문 횟수 기록
MIN_COMMAND_CNT = float('inf')  # 지금까지 나온 최소 명령 횟수

# BFS로 도착 지점에 도달하기 위한 최소 명령 횟수 찾기
BFS(start_row, start_col, start_dir)

# 결과 출력
print(MIN_COMMAND_CNT)