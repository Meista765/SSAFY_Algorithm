# 흑돌 1 백돌 2
# 4방향을 탐색하기전에 이전 돌을 한번 확인해야 한다.
def check(color):

    for i in range(N):
        for j in range(N):
            if arr[i][j] == color:
                # 탐색시작
                for k in range(4):
                    if k == 0:  # 오른쪽 탐색 하기 전 왼쪽 확인
                        if 0 <= j-1 < N and arr[i][j-1] == color:
                            continue
                    elif k == 1: # 우하향 탐색 하기 전 좌상향 확인
                        if 0 <= i-1 < N and 0 <= j-1 < N and arr[i-1][j-1] == color:
                            continue
                    elif k == 2: # 하 탐색 하기 전 위에 확인
                        if 0 <= i-1 < N and arr[i-1][j] == color:
                            continue
                    elif k == 3: # 좌하향 확인하기 전에 우상향 확인
                        if 0 <= i+1 < N and 0 <= j-1 < N and arr[i+1][j-1] == color:
                            continue
                    ni = i + di[k]
                    nj = j + dj[k]
                    cnt = 1
                    while 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == color:
                        cnt += 1
                        ni += di[k]
                        nj += dj[k]
                    if cnt == 5:
                        return color, i+1,j+1
    return -1, -1, -1


N = 19
arr = [list(map(int,input().split())) for _ in range(N)]
# 방향 설정
# 우, 우하향, 하, 좌하향
di = [0, 1, 1, -1]
dj = [1, 1, 0, 1]

black = check(1)
white = check(2)

if black[0] > white[0]:
    print(black[0])
    print(black[1], black[2])
elif black[0] == white[0]:
    print(0)
else:
    print(white[0])
    print(white[1], white[2])





