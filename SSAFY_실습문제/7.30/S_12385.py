# import sys
# sys.stdin = open("input.txt", "r")
T = int(input())

for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())  # K: 최대 이동 거리, N: 목적지, M: 충전기가 설치된 수
    arr = list(map(int, input().split()))  # 정류장

    cnt = 0  # 정류장 방문 횟수
    current = 0  # 현재 위치

    while current + K < N:  # 현재 위치가 목표 위치보다 커지면
        for i in range(K, 0, -1):  # K만큼 갈수 있을 때 최소 횟수로 가기 위해선 가능하면 K거리에 있는 정거장에 가는 게 유리
            if (current + i) in arr:
                current += i
                cnt += 1

                break
        else:  # 만약 현재 위치에서 K만큼 거리안에 정거장이 없으면 while문 벗어나서 종료 후 cnt = 0
            cnt = 0
            break

    print(f'#{test_case} {cnt}')
