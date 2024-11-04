import sys
sys.stdin = open('sample_input.txt', 'r')

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

blocks = [
    [],     # 0번
    {
        0:2,
        1:0,
        2:3,
        3:1
    },     # 1번
    {
        0:2,
        1:3,
        2:1,
        3:0
    },     # 2번
    {
        0:1,
        1:3,
        2:0,
        3:2
    },     # 3번
    {
        0:3,
        1:2,
        2:0,
        3:1
    }     # 4번
]

# 웜홀 짝 찾기
def find_wormhole(matrix):
    wormhole = [[] for _ in range(5)]

    for r in range(N):
        for c in range(N):
            if matrix[r][c] in [6, 7, 8, 9, 10]:
                wormhole[matrix[r][c] - 6].append((r, c))
    return wormhole

# 점수 계산 함수
def game_play(start_r, start_c, wormhole, start_direction):
    global max_score

    score  = 0
    current_r = start_r
    current_c = start_c
    current_direction = start_direction

    while True:
        nr = current_r + dr[current_direction]
        nc = current_c + dc[current_direction]

        if (0 <= nr < N) and (0 <= nc < N):
            value = field[nr][nc]
            current_r, current_c = nr, nc

            # 게임 종료 규칙
            if (value == -1) or ((current_r, current_c) == (start_r, start_c)):
                break
            # 사각 블럭
            elif value == 5:
                score += 1
                current_direction = (current_direction + 2) % 4
            # 다른 블럭
            elif value in [1, 2, 3, 4]:
                score += 1
                current_direction = blocks[value][current_direction]
                # 방향이 바뀐 직후 다음 갈 곳이 인덱스를 넘어갈 때
                temp_r = current_r + dr[current_direction]
                temp_c = current_c + dc[current_direction]
                if not (0 <= temp_r < N) or not (0 <= temp_c < N):
                    score += 2
                    # 벽에 부딪힌 후
                    current_direction = (current_direction + 2) % 4
                    # 다시 블럭 만나기
                    current_direction = blocks[value][current_direction]
            # 웜홀
            elif value in [6, 7, 8, 9, 10]:
                pairs =  wormhole[value - 6]
                for position in pairs:
                    if (current_r, current_c) != position:
                        current_r, current_c = position
                        break
            elif value == 0:
                # 벽을 만났을 때
                if (current_direction in [1, 3]) and (current_r in [0, N-1]):
                    score += 1
                    current_direction = (current_direction + 2) % 4
                elif (current_direction in [0, 2]) and (current_c in [0, N-1]):
                    score += 1
                    current_direction = (current_direction + 2) % 4
                continue
        # 시작부터 인덱스 넘어가는 경우
        else:
            break

    if max_score < score:
        max_score = score

for tc in range(1, int(input()) + 1):
    N = int(input())
    field = [list(map(int, input().split())) for _ in range(N)]

    # 웜홀 리스트
    wormholes = find_wormhole(field)
    
    max_score = -1

    for r in range(N):
        for c in range(N):
            if field[r][c] == 0:
                for direction in range(4):
                    game_play(r, c, wormholes, direction)

    print(f'#{tc} {max_score}')