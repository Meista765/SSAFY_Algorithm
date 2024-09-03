# 캐슬 디펜스
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
#sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")
#input = sys.stdin.readline

'''
- 각 칸에 포함된 적의 수는 최대 하나
- N+1번 행의 모든 칸에는 성이 있음
- 궁수는 성이 있는 칸에 3명만 배치
- 하나의 칸에는 최대 1명의 궁수만 있을 수 있음
- 각 턴마다 궁수는 적 하나 공격, 모든 궁수는 동시에 공격
- 궁수는 가장 가까운 적을 공격하고, 같은 거리에 적이 여럿 있으면 왼쪽 적 공격
- 같은 적이 여러 궁수에게 공격 당할 수 있음
- 궁수 공격 끝나면 적 이동 (아래로 한 칸)
- 적이 성이 있는 칸으로 이동한 경우 게임에서 제외
- 모든 적이 격자 판에서 제외되면 게임 끝
goal : 궁수의 공격으로 제거할 수 있는 적의 최대 수
0 : 빈 칸
1 : 적이 있는 칸
'''

from collections import deque

def BFS(start):
    queue = deque()
    for archer_pos in start:
        queue.append(archer_pos)
    print(queue)


N, M, D = map(int, input().split())     # N: 격자판 행 수, M: 격자판 열 수, D: 궁수 공격 거리 제한
arr = [list(map(int, input().split())) for _ in range(N)]   # 격자 판
arr += [[2] * N]                        # N+1 행에 성 만들어줌 (2는 성을 의미)
dr, dc = [-1, 0, 0], [0, -1, 1]         # 상 좌 우

# NC3 구현 (궁수 위치 정하기)
for i in range(1 << M):                 # 0부터 2^M까지 순회
    arr[-1] = [2] * N                   # N+1 행 초기화 (궁수 재배치를 위해)
    archers = [0] * M                   # 아처 위치 목록 초기화
    cnt = 0                             # 3명의 아처만 배치하기 위한 카운트 변수
    for j in range(M):                  # 0 ~ M까지 j에 차례로 넣으면서
        if i & (1 << j):                # 이진수 1의 비트를 j칸씩 왼쪽으로 밀어. 그 비트랑 i 비트랑 AND 연산
            cnt += 1                    # AND 연산 결과 True 반환되면 cnt 하나 증가
            archers[j] = 1              # 이번 위치에 1 넣기
    if cnt == 3:                        # 카운트가 3인 경우만 (아처가 3명만 배치된 경우만)
        start = []                      # BFS에 넣을 스타트 좌표 리스트
        for c in range(M):              # N+1 행에 위에서 만들어진 패턴대로 아처 좌표 뽑기
            if archers[c]:
                start.append((N, c))    # 좌표를 start에 넣어주기
        BFS(start)                      # BFS에 start 인자로 주기