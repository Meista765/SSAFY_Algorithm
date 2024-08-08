import sys
sys.stdin = open('C:/Users/SSAFY/Desktop/git/SSAFY_Algorithm/SWEA/SWEA_12394', 'r')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(input()) for _ in range(N)]


#### 현이 코드

T = int(input()) # tc
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    # ans = [0] * M
    ans = ''

    # 가로방향 탐색
    for col in range(N): # 모든행에 대해서
        for start in range(N-M+1): # 시작 인덱스의 마지막 포인트는 N-M ㄱㄴㄲ range에서는 +1
            end = start + (M-1)
            for delta in range(M//2): # 10개 문자 회문이면, 5 ; 0 1 2 3 4
                if arr[col][start + delta] != arr[col][end - delta]: #각행에서 열을 검사
                    break

            else: # 무사히 통과하면 회문!
                for j in range(start, end+1):  # j: start ~ end
                    ans += arr[col][j]

    # 세로방향 탐색
    for row in range(N): #모든 열에 대해서
        for col_st in range(N-M+1):
            # 행의 인덱스가 탐색하고자하는 회문의 길이만큼은 여유를 둬야함
            # col_st => N-M+1이 마지막 스타팅 포인트
            end = col_st + (M-1)
            for delta in range(M//2):
                if arr[col_st+delta][row] != arr[end-delta][row]:
                    break
            else: # 무사히 통과하면 회문!
                for j in range(col_st, end+1):  # j: start ~ end
                    ans += arr[j][row]