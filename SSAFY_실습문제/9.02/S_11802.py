def dfs(r,c,s):         # s: 현재까지의 합
    global min_val
 
    # 가지치기
    if s > min_val:
        return
 
    if r == N-1 and c == N-1:
        min_val = s
 
    # 오른쪽으로 이동
    if c + 1 < N:
        dfs(r, c + 1, s + arr[r][c+1])
    # 아래로 이동
    if r + 1 < N:
        dfs(r + 1, c, s + arr[r+1][c])
 
 
T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    min_val = 13 * (N * 2 -1)
    dfs(0,0,arr[0][0])
    print(f'#{test_case} {min_val}')