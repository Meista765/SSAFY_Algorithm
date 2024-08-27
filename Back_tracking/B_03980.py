# 선발 명단
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
#sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")
#input = sys.stdin.readline

def backtrack(pos, stat_sum):        # pos: 포지션 번호, stat_sum: 현재까지의 능력치 합
    global max_sum, visited

    if pos == 11:                    # 11번(인덱스로 10) 포지션까지 다 돌았으면
        if stat_sum > max_sum:       # 능력치 합이 기존 최댓값을 넘겼으면
            max_sum = stat_sum       # 최댓값 갱신
        return                       # 해당 경로 종료

    for player in range(11):                        # 해당 포지션에 대해 11명의 선수 능력치 탐색
        stat = stats[player][pos]                   # 해당 선수 능력치 가져와서
        if stat and not visited[player]:            # 능력치가 0이 아니면서 방문한적 없는 선수일 때
            visited[player] = 1                     # 방문 표시
            backtrack(pos + 1, stat_sum + stat)     # 다음 포지션으로 넘어가면서 능력치 합에 해당 선수 능력치 넣기
            visited[player] = 0                     # 해당 경로 재귀가 끝나고 다시 돌아오면서 방문 리스트 초기화

for _ in range(int(input())):
    stats = [list(map(int, input().split())) for _ in range(11)]    # 능력치 배열 (행: 선수, 열: 포지션)
    max_sum = 0                 # 능력치 최댓값 초기화
    visited = [0] * 11          # 방문 리스트 초기화
    backtrack(0, 0)             # 0번 포지션, 능력치 합 0에서 시작
    print(max_sum)              # 능력치 합 최댓값 출력