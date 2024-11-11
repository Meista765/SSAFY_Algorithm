import sys
sys.stdin = open('sample_input.txt', 'r')

dr = [-1, -1, 1, 1]
dc = [1, -1, -1, 1]

def cafe_tour(start_r, start_c, start_direction):
    global max_count

    ate = {field[start_r][start_c]}
    current_r, current_c = (start_r, start_c)
    visit_cnt = 1                               # 현재까지 방문한 카페 수
    switch_cnt = 0                              # 방향 전환 횟수
    
    current_direction = start_direction
    formal_attempt = False

    while True:
        nr = current_r + dr[current_direction]
        nc = current_c + dc[current_direction]

        # 앞으로 나아가지 않고 방향 전환만 할 때는 formal_attempt를 True로 바꾸어준다
        # formal_attempt가 True인데 또 다시 방향만 바꿀 경우 바로 함수 종료
        # 인덱스 벗어날 때
        if not (0 <= nr < N) or not (0 <= nc < N):
            # 첫 시작부터 벗어나도 어차피 다른 방향 탐색하니까 종료
            if formal_attempt or visit_cnt == 1:
                return
            else:
                current_direction = (current_direction + 1) % 4
                switch_cnt += 1
                if switch_cnt > 3:
                    return
                formal_attempt = True
        # 이미 먹은 디저트일 때
        elif field[nr][nc] in ate:
            # 시작 지점으로 돌아왔다면
            if (nr, nc) == (start_r, start_c):
                max_count = max(max_count, visit_cnt)
                return 
            elif visit_cnt == 1:
                current_direction = (current_direction + 1) % 4
            # 그 외의 경우 -> 방향만 바꾸기
            else:
                if formal_attempt:
                    return
                else:
                    current_direction = (current_direction + 1) % 4
                    switch_cnt += 1
                    if switch_cnt > 3:
                        return
                    formal_attempt = True
        # 앞으로 나아갈 경우, formal_attempt 다시 False로
        else:
            ate.add(field[nr][nc])
            visit_cnt += 1
            current_r, current_c = nr, nc
            formal_attempt = False

for tc in range(1, int(input()) + 1):
    N = int(input())
    
    field = [list(map(int, input().split())) for _ in range(N)]

    max_count = -1

    for r in range(N):
        for c in range(N):
            for i in range(4):
                cafe_tour(r, c, i)
    
    print(f'#{tc} {max_count}')