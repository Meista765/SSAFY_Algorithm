import sys
sys.stdin = open('input.txt')

def backtrack(v,level, cur_sum):
    global min_val
    # 가지치기
    if cur_sum > min_val:
        return

    if level == N:
        min_val = cur_sum
        return

    else:
        for i in range(0,N):
            if visited[i] == 0: # 방문하지 않은 곳이라면
                visited[i] = 1
                backtrack(v+1,level+1, cur_sum+arr[v][i])
                visited[i] = 0


T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    min_val = 99 * N
    visited = [0] * N
    backtrack(0,0,0)
    print(f'#{test_case} {min_val}')