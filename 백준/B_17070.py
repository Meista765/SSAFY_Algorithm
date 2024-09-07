#############   BFS 풀이 시간 초과 ㅜㅜ     #########################
# from collections import deque
# import sys
# input = sys.stdin.readline
#
# def bfs(r,c,d):         # r: 행 좌표, c: 열 좌표, d: 방향(가로=1, 세로=2, 대각선=3)
#     global cnt
#     q = deque()
#     q.append((r, c, d))
#
#     while q:
#         v = q.popleft()
#         # 종료 조건
#         if v[0] == N-1 and v[1] == N-1:
#             cnt += 1
#             continue
#         # 가로 일때
#         if v[2] == 1:
#             # 가로 방향으로 놓는 경우
#             if v[1] + 1 < N and arr[v[0]][v[1]+1] == 0:
#                 q.append((v[0], v[1] + 1, 1))
#             # 대각선으로 놓은 경우
#             if v[0] + 1 < N and v[1] + 1 < N and arr[v[0]+1][v[1]+1] == 0 and arr[v[0]+1][v[1]] == 0 and arr[v[0]][v[1]+1] == 0:
#                 q.append((v[0] + 1, v[1] + 1, 3))
#         # 세로일때
#         elif v[2] == 2:
#             # 세로 방향으로 놓은 경우
#             if v[0] + 1 < N and arr[v[0]+1][v[1]] == 0:
#                 q.append((v[0]+1, v[1], 2))
#             # 대각선으로 놓는 경우
#             if v[0] + 1 < N and v[1] + 1 < N and arr[v[0]+1][v[1]+1] == 0 and arr[v[0]+1][v[1]] == 0 and arr[v[0]][v[1]+1] == 0:
#                 q.append((v[0] + 1, v[1] + 1, 3))
#         # 대각선일때
#         elif v[2] == 3:
#             # 가로로 놓는 경우
#             if v[1] + 1 < N and arr[v[0]][v[1]+1] == 0:
#                 q.append((v[0], v[1] + 1, 1))
#             # 세로로 놓는 경우
#             if v[0] + 1 < N and arr[v[0]+1][v[1]] == 0:
#                 q.append((v[0]+1, v[1], 2))
#             # 대각선으로 놓는 경우
#             if v[0] + 1 < N and v[1] + 1 < N and arr[v[0]+1][v[1]+1] == 0 and arr[v[0]+1][v[1]] == 0 and arr[v[0]][v[1]+1] == 0:
#                 q.append((v[0] + 1, v[1] + 1, 3))
#
# N = int(input())
# arr = [list(map(int,input().split())) for _ in range(N)]
# cnt = 0
# bfs(0,1,1)
# print(cnt)

########## DP 풀이 #############
#
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(3)]  # 가로: 0, 세로: 1, 대각선: 2

# dp 초기화
dp[0][0][1] = 1
for i in range(2,N):    # 초기에 (0,1)까지 파이프가 있으므로 2부터 시작
    if arr[0][i] == 0:
        dp[0][0][i] = dp[0][0][i-1]


# 1행 1열 제와

for i in range(1,N):
    for j in range(1,N):
        # 가로 세로 놓기
        if arr[i][j] == 0:
            # 가로
            dp[0][i][j] = dp[0][i][j-1] + dp[2][i][j-1]
            # 세로
            dp[1][i][j] = dp[1][i-1][j] + dp[2][i-1][j]
        # 대각선 놓기
        if arr[i][j] == 0 and arr[i-1][j] == 0 and arr[i][j-1] == 0:
            dp[2][i][j] = dp[0][i-1][j-1] + dp[1][i-1][j-1] + dp[2][i-1][j-1]

cnt = dp[0][N-1][N-1] + dp[1][N-1][N-1] + dp[2][N-1][N-1]
print(cnt)