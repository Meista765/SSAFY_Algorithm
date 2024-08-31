'''
풀이방법

1단계. DFS를 활용해 인접을 제외한 모든 경우의 수를 찾는다.
-> 25C7중 S_cnt >= 4 인 경우를 확인
2단계. 찾은 경우의 수에서 BFS를 통해 인접한지 확인한다.
'''

from collections import deque

def bfs():
    visited_bfs = [[0] * 5 for _ in range(5)]     # bfs에서 활용할 방문리스트
    # 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    s = find_one()         # 시작위치
    q = deque()
    q.append(s)
    visited_bfs[s[0]][s[1]] = 1     # 방문표시
    check_cnt = 1               # 인접한 경우인지 확인 7이면 인접, 7이 아니면 인접 x
    while q:
        v = q.popleft()
        for k in range(4):
            nr = v[0] + dr[k]
            nc = v[1] + dc[k]
            if 0 <= nr < 5 and 0 <= nc < 5 and visited_bfs[nr][nc] == 0 and visited[nr][nc] == 1:
                q.append((nr,nc))
                visited_bfs[nr][nc] = 1
                check_cnt += 1

    if check_cnt == 7:
        return True
    else:
        return False



def find_one():
    for i in range(5):
        for j in range(5):
            if visited[i][j] == 1:
                return (i,j)


def back_track(k,n,s_cnt,y_cnt):    # k: 0~24, n: 선택 된 학생수, s_cnt: 다솜파 학생수, y_cnt: 도연파 학생 수
    global cnt
    # 도연 파 학생 수가 3 넘어가면 종료
    if y_cnt > 3:
        return
    # 선택하는 학생 수가 7 넘어가면 종료
    if n > 7:
        return

    if k == 25:
        if n == 7 and s_cnt >= 4:       # 포함된 학생 수가 7이고 다솜파 학생이 4 이상이면 인접한 경우인지 확인
            if bfs():
                cnt += 1
        return

    else:
        back_track(k + 1, n, s_cnt, y_cnt)      # 포함안할 때

        # 포함할 때 다솜파인지 도연파인지 경우를 나눠서 처리함
        visited[k // 5][k % 5] = 1              # 방문 표시
        if arr[k // 5][k % 5] == 'S':
            back_track(k + 1, n + 1, s_cnt + 1, y_cnt)
        else:
            back_track(k + 1, n + 1, s_cnt, y_cnt + 1)
        visited[k // 5][k % 5] = 0              # 방문 해제



# S: 다솜, Y: 임도연

arr = [input() for _ in range(5)]    # 학생 배치도
visited = [[0] * 5 for _ in range(5)]
cnt = 0
back_track(0,0,0,0)
print(cnt)