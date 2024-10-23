# 치즈
import sys
from collections import deque
#sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")
#input = sys.stdin.readline

def BFS():
    global HOURS, before_cheese_cnt
    
    cheese_surface = []
    visited = [[0] * COL for _ in range(ROW)]
    visited[0][0] = 1
    
    
    queue = deque()
    queue.append((0, 0))
    
    while queue:
        r, c = queue.popleft()
        
        for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + d[0], c + d[1]
            if 0 <= nr < ROW and 0 <= nc < COL and not visited[nr][nc]:
                if arr[nr][nc] == 1:                    # 치즈 표면이면
                    cheese_surface.append((nr, nc))     # 좌표 저장
                else:                                   # 공기면
                    queue.append((nr, nc))              # 큐에 넣기
                visited[nr][nc] = 1                     # 방문 표시
    
    # 치즈 표면이 하나도 없다는 것은 치즈가 아예 다 녹아 하나도 없는 상태라는 것
    if not cheese_surface:
        return 0
    
    # 표면 치즈 개수 세기 (모두 녹았을 때는 갱신이 안됨)
    before_cheese_cnt = len(cheese_surface)
    
    # 치즈 표면 다 녹이기
    HOURS += 1      # 1시간 걸림
    for r, c in cheese_surface:
        arr[r][c] = 0
        
    return 1


ROW, COL = map(int, input().split())    # 가로, 세로
arr = [list(map(int, input().split())) for _ in range(ROW)]     # 배열
HOURS = 0       # 치즈 다 녹는 데 걸리는 시간
# 모두 녹기 한 시간 전에 남아있는 치즈조각 개수를 세어야 하므로 
# 그냥 다 녹을 때까지 매 시간마다 세면서 갱신
before_cheese_cnt = 0
result = 1   # BFS 결과 변수 (다 녹았으면 0을 반환하고 그 전까지는 계속 1 반환)

while result:
    result = BFS()

print(HOURS)
print(before_cheese_cnt)