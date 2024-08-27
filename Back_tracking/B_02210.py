# 숫자판 점프
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
#sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")
#input = sys.stdin.readline

def backtrack(row, col, string):
    global cases
    if len(string) == 6:                        # 6자리 숫자가 되면
        if string not in cases:                 # 지금까지 아직 나온적 없는 케이스면
            cases.append(string)                # 새로운 케이스 추가
        return                                  # 현재 재귀 경로 종료
    for k in range(4):                          # 상하좌우 탐색
        nr = row + dr[k]
        nc = col + dc[k]
        if 0 <= nr < 5 and 0 <= nc < 5:         # 한번 거쳤던 칸은 다시 거쳐도 되니 방문리스트 필요 없음
            backtrack(nr, nc, string + arr[nr][nc])


arr = [input().split() for _ in range(5)]       # 숫자 판
dr = [0, 0, 1, -1]                              # 행 델타
dc = [1, -1, 0, 0]                              # 열 델타
cases = []                                      # 만들 수 있는 서로 다른 여섯자리의 수 케이스

# 모든 칸을 순회하며 시작점으로 설정
for r in range(5):
    for c in range(5):
        backtrack(r, c, arr[r][c])

print(len(cases))