'''
문자	의미
.	평지(전차가 들어갈 수 있다.)
*	벽돌로 만들어진 벽
#	강철로 만들어진 벽
-	물(전차는 들어갈 수 없다.)
^	위쪽을 바라보는 전차(아래는 평지이다.)
v	아래쪽을 바라보는 전차(아래는 평지이다.)
<	왼쪽을 바라보는 전차(아래는 평지이다.)
>	오른쪽을 바라보는 전차(아래는 평지이다.)
'''
'''
2 2
<.
..
12
DDSRRSUUSLLS
'''
import sys
sys.stdin = open('input.txt')

def command(arr,cmd,N,location): # 맵, 명령, 명령의 수, 위치

    if cmd == 'U':   # 전차의 방향을 바꾸고 앞이 평지이면 앞으로 전진
        if 0 <= location[0]-1 < H and arr[location[0]-1][location[1]] == '.': # 맵을 벗어나지 않고 위의 칸이 평지라면
            arr[location[0]][location[1]] = '.'         # 현재 위치를 평지로 바꾸고
            location[0] -= 1                            # 탱크의 위치를 바꾼다.
            arr[location[0]][location[1]] = tank[0]     # 맵에 이동한 탱크의 위치 반영
        else:                                           # 평지가 아니면
            arr[location[0]][location[1]] = tank[0]     # 방향만 바꾼다.

    elif cmd == 'D':
        if 0 <= location[0]+1 < H and arr[location[0]+1][location[1]] == '.': # 맵을 벗어나지 않고 아래의 칸이 평지라면
            arr[location[0]][location[1]] = '.'         # 현재의 위치를 평지로 바꾸고
            location[0] += 1                            # 탱크의 위치를 바꾼다.
            arr[location[0]][location[1]] = tank[1]     # 맵에 이동한 탱크의 위치 반영
        else:                                           # 평지가 아니면
            arr[location[0]][location[1]] = tank[1]     # 방향만 변경

    elif cmd == 'R':
        if 0 <= location[1] + 1 < W and arr[location[0]][location[1]+1] == '.':  # 맵을 벗어나지 않고 오른쪽 칸이 평지라면
            arr[location[0]][location[1]] = '.'         # 현재의 위치를 평지로 바꾸고
            location[1] += 1                            # 탱크의 위치를 바꾼다.
            arr[location[0]][location[1]] = tank[2]     # 맵에 이동한 탱크의 위치 반영
        else:                                           # 평지가 아니면
            arr[location[0]][location[1]] = tank[2]     # 방향만 변경

    elif cmd == 'L':
        if 0 <= location[1] -1 < W and arr[location[0]][location[1]-1] == '.':  # 맵을 벗어나지 않고 오른쪽 칸이 평지라면
            arr[location[0]][location[1]] = '.'         # 현재의 위치를 평지로 바꾸고
            location[1] -= 1                            # 탱크의 위치를 바꾼다.
            arr[location[0]][location[1]] = tank[3]     # 맵에 이동한 탱크의 위치 반영
        else:                                           # 평지가 아니면
            arr[location[0]][location[1]] = tank[3]     # 방향만 변경

    elif cmd == 'S':
        if arr[location[0]][location[1]] == tank[0]:    # 현재 탱크가 위쪽 방향을 보고 있다면
            ni = location[0] -1
            while 0 <= ni < H and arr[ni][location[1]] != '*' and arr[ni][location[1]] != '#': # 벽이 아니면 계속진행
                ni -= 1
            if 0 <= ni < H and arr[ni][location[1]] == '*':     # 벽돌을 만나서 멈춘 거면
                arr[ni][location[1]] = '.'      # 평지로 바꾸기

        elif arr[location[0]][location[1]] == tank[1]:  # 현재 탱크가 아래쪽 방향을 보고 있다면
            ni = location[0] +1
            while 0 <= ni < H and arr[ni][location[1]] != '*' and arr[ni][location[1]] != '#': # 벽이 아니면 계속진행
                ni += 1
            if 0 <= ni < H and arr[ni][location[1]] == '*':     # 벽돌을 만나서 멈춘 거면
                arr[ni][location[1]] = '.'      # 평지로 바꾸기

        elif arr[location[0]][location[1]] == tank[2]:  # 현재 탱크가 오른쪽 방향을 보고 있다면
            nj = location[1] +1
            while 0 <= nj < W and arr[location[0]][nj] != '*' and arr[location[0]][nj] != '#': # 벽이 아니면 계속진행
                nj += 1
            if 0 <= nj < W and arr[location[0]][nj] == '*':  # 벽돌을 만나서 멈춘 거면
                arr[location[0]][nj] = '.'   # 평지로 바꾸기
        elif arr[location[0]][location[1]] == tank[3]:  # 현재 탱크가 왼쪽 방향을 보고 있다면
            nj = location[1] -1
            while 0 <= nj < W and arr[location[0]][nj] != '*' and arr[location[0]][nj] != '#': # 벽이 아니면 계속진행
                nj -= 1
            if 0 <= nj < W and arr[location[0]][nj] == '*':  # 벽돌을 만나서 멈춘 거면
                arr[location[0]][nj] = '.'   # 평지로 바꾸기


T = int(input())
for test_case in range(1,T+1):
    H, W= map(int,input().split())      # H: 높이, W: 너비
    arr = [list(input()) for _ in range(H)]   # 게임 맵
    N = int(input())    # 명령의 수
    cmd = input()       # 명령

    tank = ['^', 'v', '>', '<']  # tank의 위치 및 방향

    # 탱크 좌표 찾기
    location = [0,0]
    for i in range(H):
        for j in range(W):
            if arr[i][j] in tank:
                location[0] =i
                location[1] = j
                break

    for c in range(N):
        command(arr, cmd[c], N, location)
    print(f'#{test_case}', end=' ')
    for i in range(H):
        print(''.join(arr[i]))


