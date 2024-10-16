# 모래성
import sys
#sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")
#input = sys.stdin.readline

H, W = map(int, input().split())                # 격자 가로 세로 크기
grid = [list(input()) for _ in range(H)]        # 격자
dr = [0, 0, 1, -1, 1, 1, -1, -1]                # 행 델타
dc = [1, -1, 0, 0, -1, 1, -1, 1]                # 열 델타

wave_num = 0      # 파도 횟수

while True:
    destroyed = []                            # 파괴되는 블럭 좌표 리스트
    for r in range(H):
        for c in range(W):
            if grid[r][c] != '.':             # 숫자면
                cnt = 0                       # 카운트 초기화
                # 8방향에 있는 '.' 개수만큼 카운트 올리기
                for k in range(8):
                    nr = r + dr[k]
                    nc = c + dc[k]
                    # 그리드 범위 안이고, '.'이면 카운트 증가
                    if 0 <= nr < H and 0 <= nc < W and grid[nr][nc] == '.':
                        cnt += 1
                # 카운트가 현재 위치 튼튼함 정도보다 크거나 같으면 리스트에 저장         
                if cnt >= int(grid[r][c]):         
                    destroyed.append([r, c])
    
    # 모래성에 변화가 없었으면 반복 종료
    if not destroyed:
        break
    
    # 리스트에 저장된 모든 파괴할 블록을 '.'으로 바꾸기
    while destroyed:
        row, col = destroyed.pop()
        grid[row][col] = '.'
    
    wave_num += 1      # 파도 한번 쳤음

print(wave_num)