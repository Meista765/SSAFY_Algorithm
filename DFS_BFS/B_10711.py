# 모래성
import sys
from collections import deque
#sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")
#input = sys.stdin.readline

def BFS():
    queue = deque()      # 빈 큐 만들기
    
    # '.'인 칸 좌표를 큐에 넣기 / '.'는 모두 0으로 바꾸기 / 숫자 칸 데이터 타입 int로 바꾸기
    for r in range(H):
        for c in range(W):
            if grid[r][c] == '.':
                queue.append([r, c, 0])
                grid[r][c] = 0
            else:
                grid[r][c] = int(grid[r][c])
    
    while queue:
        # 큐에서 '.' 좌표, 파도 횟수 정보 빼내기
        r, c, wave = queue.popleft()
        # '.' 주변 8방향 탐색   
        for k in range(8):
            nr = r + dr[k]
            nc = c + dc[k]
            # '.' 주변에 있는 숫자들 모두 1 감소시키기
            if 0 <= nr < H and 0 <= nc < W and grid[nr][nc]:
                grid[nr][nc] -= 1
                # 모래성이 무너졌으면
                if grid[nr][nc] == 0:
                    # 무너진 부분 좌표, 파도횟수+1 정보를 큐에 넣기
                    queue.append([nr, nc, wave+1])    

    return wave


H, W = map(int, input().split())                # 격자 가로 세로 크기
grid = [list(input()) for _ in range(H)]        # 격자
dr = [0, 0, 1, -1, 1, 1, -1, -1]                # 행 델타
dc = [1, -1, 0, 0, -1, 1, -1, 1]                # 열 델타

# BFS 함수 호출하고, 리턴 값인 파도 횟수 출력            
print(BFS())