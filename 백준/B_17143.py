import sys
sys.stdin = open('B_17143.txt')

# 물고기 잡기
def fishing():
    global fishing_king
    fishing_king += 1
    for i in range(R):
        if arr[i][fishing_king]:
            size = arr[i][fishing_king][2]
            arr[i][fishing_king][2] = []
            break
    return size


R, C, M = map(int,input().split())
arr = [[[] for _ in range(C)] for _ in range(R)]

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    arr[r-1][c-1].append([s ,d ,z])     # 속력, 이동방향, 크기

# 상하우좌
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]


fishing_king = -1           # 낚시왕 초기 위치

'''
상어가 움직이는 것을 어떻게 표현해야될까?
'''
for i in range(R):
    print(*arr[i])