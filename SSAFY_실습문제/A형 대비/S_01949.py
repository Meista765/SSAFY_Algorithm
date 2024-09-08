'''
해결방법:
1. dfs 이용
2. 제일 큰 수를 찾고 제일 큰 수를 가지는 좌표를 저장
3. 저장된 좌표로 dfs 탐색 시작
4. dfs를 탐색하면 자신보다 작으면 다음좌표로 이동 지신보다 같거나 크면 다음 높이가 현재 높이 + K 보다 큰지 작은지 확인
5. 작으면 다음 높이를 현재 높이의 -1로 바꿈
!!! 주의사항 !!!
1. 산을 깎았으면 원상복구
2. 방문 체크도 원상복구
'''


import sys
sys.stdin = open('input.txt')


def find_top():
    global max_val

    for i in range(N):
        for j in range(N):
            if arr[i][j] > max_val:
                max_val = arr[i][j]

def dfs(s,d,K):                 # s: 좌표, d: 현재까지의 거리, K: 최대 공사 깊이
    global max_len
    # 최대값 갱신
    if d > max_len:
        max_len = d

    visited[s[0]][s[1]] = 1         # 방문 표시

    for k in range(4):
        nr = s[0] + dr[k]
        nc = s[1] + dc[k]

        if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:        # 인덱스를 벗어나지 않고
            if arr[nr][nc] < arr[s[0]][s[1]]:                           # 땅 안파도 이동이 가능하다면
                dfs((nr,nc), d+1, K)
            elif K != 0 and arr[nr][nc] - K < arr[s[0]][s[1]]:
                tmp = arr[nr][nc]                                       # 원상복구를 위해 값을 저장해준다.
                arr[nr][nc] = arr[s[0]][s[1]] - 1                       # 최대한 적게 파야 되기 때문에 현재 좌표에서 1 작은 값으로 바꿔준다.
                dfs((nr,nc), d+1, 0)
                arr[nr][nc] = tmp

    visited[s[0]][s[1]] = 0     # 방문 초기화


T = int(input())
for test_case in range(1,T+1):
    N, K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    max_val = 0
    find_top()              # 함수호출
    top = []                # 제일 높은 봉우리를 저장할 리스트
    max_len = 0             # 제일 긴 등산로
    visited = [[0] * N for _ in range(N)]  # 방문 리스트 생성
    # 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 제일 높은 봉우리의 좌표를 저장
    for i in range(N):
        for j in range(N):
            if arr[i][j] == max_val:
                top.append((i,j))


    for s in top:
        dfs(s, 1, K)

    print(f'#{test_case} {max_len}')
    # print(max_val)


