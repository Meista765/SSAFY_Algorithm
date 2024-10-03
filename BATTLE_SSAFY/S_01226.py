# [S/W 문제해결 기본] 7일차 - 미로1
import sys
sys.stdin = open('C:/Users/82108/Downloads/sample_input.txt', 'r')

def DFS(cur_r, cur_c):
    global arrive
    if arr[cur_r][cur_c] == '3':
        arrive = True
        return
    
    if arrive:
        return
    
    for k in range(4):
        nr = cur_r + dr[k]
        nc = cur_c + dc[k]
        if 0 <= nr < 16 and 0 <= nc < 16 and arr[nr][nc] != '1' and not visited[nr][nc]:
            visited[nr][nc] = 1
            DFS(nr, nc)


for _ in range(10):
    tc = int(input())
    arr = [list(input()) for _ in range(16)]
    dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]
    visited = [[0] * 16 for _ in range(16)]
    arrive = False
    
    # 미로 시작점 찾기
    for r in range(16):
        for c in range(16):
            if arr[r][c] == '2':
                cur_r, cur_c = r, c
                break
    
    visited[cur_r][cur_c] = 1
    DFS(cur_r, cur_c)
    if arrive: ans = 1
    else: ans = 0
    print(f'#{tc}', ans)