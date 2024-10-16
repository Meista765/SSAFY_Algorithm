import sys
sys.stdin = open('sample_input.txt', 'r')

def permutation(k, N):
    global min_sum
    sum_value = 0
    if k == N:
        for i in range(N):
            sum_value +=  matrix[i][arr[i]]
            if sum_value > min_sum:
                return
        if sum_value < min_sum:
            min_sum = sum_value
            return
    else:
        for i in range(k, N):
            arr[k], arr[i] = arr[i], arr[k]
            permutation(k + 1, N)
            arr[k], arr[i] = arr[i], arr[k] 

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    arr = list(range(N))
    min_sum = 10 * N
    
    permutation(0, N)
    
    print(f'#{tc} {min_sum}')


#============================================================================

def dfs(n,sm) :
    global ans
 
    # 가지치기
    if sm >= ans :
        return
 
 
    if n == N :
        # 최솟값 갱신
        ans = min(ans,sm)
        return
     
    # n : 행, j : 열 / 하나씩 확인해보기
    for j in range(N) :
        if visit[j] == 0 :
            visit[j] = 1
            dfs(n+1, sm+arr[n][j])
            visit[j] = 0
 
 
T = int(input())
for tc in range(1,T+1) :
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    ans = 999999999999
    visit = [0] * N     # 열 사용 표시
 
    dfs(0,0)
 
    print(f'#{tc} {ans}')

