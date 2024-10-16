# 인구 이동
import sys
from collections import deque
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
#sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")
#input = sys.stdin.readline

DEBUG = 1


def BFS(start, move_cnt):
    pass



N, L, R = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
days = 0

if DEBUG:
    print('L :', L)
    print('R :', R)
    print('<배열>')
    for i in range(N):
        print(*arr[i])
    print()

while True:
    days += 1       # 하루 지남
    for r in range(N):
        for c in range(N):
            move_cnt = 0    # 이동 발생 호
            BFS((r, c), move_cnt)
            
            if move_cnt == 0:    # 이동이 발생하지 않았을 경우
                days -= 1        # 아까 올렸던거 하나 내리고
                break            # 반복문 종료