import sys
sys.stdin = open('B_17143.txt')

# 물고기 잡기
def fishing():
    for i in range(R):
        if arr[i][fishing_king]:
            size = arr[i][fishing_king][0][2]
            arr[i][fishing_king] = []
            return size
    return 0
# 상어 움직이기
def move():
    temp = [[[] for _ in range(C)] for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if arr[i][j]:               # 빈 리스트가 아니라면....
                r, c = i, j
                s, d, z = arr[i][j][0]
                distance = s
                while distance:                # 거리가 0이 될때 까지
                    r = r + dr[d]
                    c = c + dc[d]
                    if 0 <= r < R and 0 <= c < C:
                        distance -= 1
                    else:
                        r -= dr[d]
                        c -= dc[d]
                        if d == 0:
                            d = 1
                        elif d == 1:
                            d = 0
                        elif d == 2:
                            d = 3
                        elif d == 3:
                            d = 2

                temp[r][c].append([s,d,z])
    # 큰 상어 남기기
    for i in range(R):
        for j in range(C):
            if len(temp[i][j]) >= 2:
                temp[i][j] = [max(temp[i][j], key=lambda x:x[2])]
    return temp



R, C, M = map(int,input().split())
arr = [[[] for _ in range(C)] for _ in range(R)]

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    arr[r-1][c-1].append([s,d-1,z])     # 속력, 이동방향, 크기


# 상하우좌
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]


fishing_king = 0           # 낚시왕 초기 위치

total_size = 0
while fishing_king < C:
    size= fishing()

    total_size += size
    arr = move()
    fishing_king += 1
print(total_size)