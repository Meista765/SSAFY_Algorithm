# 차윤이의 RC카
import sys
sys.stdin = open('C:/Users/82108/Downloads/sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    N = int(input())    # 필드의 크기 (2 ~ 5)
    arr = [list(input()) for _ in range(N)]     # 필드
    
    # 출발지점 찾기
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 'X':
                start_r, start_c = r, c
                break
    
    Q = int(input())    # 조종한 횟수 (1 ~ 5)
    dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]   # 방향: 0 1 2 3 -> 상 우 하 좌
    for _ in range(Q):
        C, command = input().split()
        dir = 0                             # 항상 시작 방향은 상(0)
        cur_r, cur_c = start_r, start_c     # 현재 위치를 시작 위치로 설정
    
        # 커맨드 실행
        for c in command:
            if c == 'A':
                nr = cur_r + dr[dir]
                nc = cur_c + dc[dir]
                if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != 'T':
                    cur_r, cur_c = nr, nc
            elif c == 'L':
                dir -= 1
                if dir == -1:
                    dir = 3
            elif c == 'R':
                dir += 1
                if dir == 4:
                    dir = 0
        
        # 커맨드가 끝났을 때 Y에 도달해 있는지 확인
        if arr[cur_r][cur_c] == 'Y':
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()