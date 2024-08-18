def check(arr):

    cnt = 0     # 빙고 갯수
    # 가로 탐색
    for i in range(5):
        if arr[i] == [0,0,0,0,0]:
            cnt += 1

    # 세로 탐색
    for j in range(5):
        tmp = 0
        for i in range(5):
            if arr[i][j] == 0:
                tmp += 1
        if tmp == 5:
            cnt += 1

    # 우하향 대각선
    tmp = 0
    for i in range(5):
        if arr[i][i] == 0:
            tmp += 1
    if tmp == 5:
        cnt += 1

    # 좌하향 대각선
    tmp =0
    for i in range(5):
        if arr[i][5-1-i] ==0:
            tmp += 1
    if tmp == 5:
        cnt += 1

    return cnt

arr = [list(map(int,input().split())) for _ in range(5)]
number = []
for _ in range(5):
    number += list(map(int,input().split()))

speak_cnt = 0
for n in range(25):
    speak_cnt += 1
    for i in range(5):
        for j in range(5):
            if number[n] == arr[i][j]:
                arr[i][j] = 0
    if speak_cnt >= 12: # 최소 12 번 불러야 빙고 3이 나옴
        result = check(arr)
        if result >= 3:
            print(speak_cnt)
            break



