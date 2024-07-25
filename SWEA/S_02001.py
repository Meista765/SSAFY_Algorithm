'''
- 문제번호  : 2001
- 문항명    : 파리퇴치
- 핵심      : 구간합
'''
import sys
sys.stdin = open('C:/Users/wns95/Downloads/input.txt', 'r')

# Test case 입력
T = int(input())

for tc in range(1, T+1):
    # Matrix Size(N), 파리채 Size(M) 입력
    N, M = map(int, input().split())
    
    # Matrix 입력
    A = [[0 for _ in range(N+1)]]
    for _ in range(N):
        A.append([0] + list(map(int, input().split())))
    
    # 부분합 초기화
    S = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for i in range(1, N+1): # i: 1 ~ N
        for j in range(1, N+1): # j: 1 ~ N
            S[i][j] = A[i][j] + S[i-1][j] + S[i][j-1] - S[i-1][j-1]
    
    # 정답을 저장하는 변수
    ans = 0
    
    # 범위를 탐색하며 정답 탐색
    for i in range(M, N+1): # i: N-M-1 ~ N
        for j in range(M, N+1): # j: N-M-1 ~ N
            now = S[i][j] - S[i-M][j] - S[i][j-M] + S[i-M][j-M]
            if ans < now:
                ans = now
    
    
    print(f'#{tc} {ans}')