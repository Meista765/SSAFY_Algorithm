import sys
sys.stdin =open('input2.txt','r')

for test_case in range(1,11):
    T = int(input())
    ladder = [[0] * (100+2)] +[[0] + list(map(int,input().split())) + [0] for _ in range(100)] + [[0] * (100+2)] # 0으로 둘러 싸기
    # 2좌표 찾기
    for start in range(1,102):
        if ladder[100][start] == 2:
            break


    x = start       # 현재 x좌표
    y = 100     # 현재 y좌표

    while y != 1:
        if ladder[y][x-1] == 1: # 왼쪽에 길이 있을 때
            x -= 1              # x좌표 -1 -> 왼쪽으로
            ladder[y][x] = 0    # 지나온 길 0으로 -> 안하면 무한 루프

        elif ladder[y][x+1] == 1: # 오른쪽에 길이 있을 때
            x += 1                # x좌표 +1 -> 오른쪽으로
            ladder[y][x] = 0

        elif ladder[y-1][x] == 1: # 둘다 없으면 위로
            y -= 1
            ladder[y][x] = 0

    print(f'#{T} {x-1}')


