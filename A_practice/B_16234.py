# 인구 이동
import sys
from collections import deque
#sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")
#input = sys.stdin.readline

DEBUG = 0

def BFS(start):
    global visited, move_cnt
    
    union = [start]      # 연합 목록
    
    queue = deque()
    queue.append(start)
    
    while queue:
        r, c = queue.popleft()
        for dr, dc in [(1,0),(0,1),(-1,0),(0,-1)]:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                if L <= abs(arr[r][c] - arr[nr][nc]) <= R:
                    union.append((nr, nc))
                    move_cnt += 1
                    visited[nr][nc] = 1
                    queue.append((nr, nc))
    
    result = sum(arr[r][c] for r, c in union) // len(union)
    for r, c in union:
        arr[r][c] = result


N, L, R = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
days = 0

if DEBUG:
    print('L :', L)
    print('R :', R)
    print('<배열>')
    for i in range(N):
        print(*arr[i])
    print()

while True:
    days += 1            # 하루 지남
    visited = [[0] * N for _ in range(N)]
    move_cnt = 0         # 이동 발생 횟수
    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                visited[r][c] = 1
                BFS((r, c))

    if DEBUG:
        print('<업데이트 된 배열>')
        for i in range(N):
            print(*arr[i])
        print()
    
    if move_cnt == 0:    # 이동이 발생하지 않았을 경우
        days -= 1        # 아까 올렸던거 하나 내리고
        break            # 반복문 종료

print(days)