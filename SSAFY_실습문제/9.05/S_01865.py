import sys
sys.stdin = open('input.txt')

def backtrack(k,cur_mul):
    global max_val
    if cur_mul < max_val:   # 0보다 작은 수를 계속 곱하는 과정에서 현재 값이 최대값보다 작으면 어떤 0보다 작은 수를 곱해도 작아짐
        return
    if k == N:
        max_val = cur_mul
    else:
        for i in range(N):
            if visited[i] or arr[k][i] == 0:        # 곱할 수 인 arr[k][i] = 0 이면 확인 곱할 필요 없음
                continue
            visited[i] = 1
            backtrack(k+1,cur_mul * arr[k][i])
            visited[i] = 0


T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr = [list(map(lambda x: float(x) / 100, input().split())) for _ in range(N)]
    visited = [0] * N
    max_val = 0
    backtrack(0,1)
    print(f'#{test_case} {max_val* 100:.6f}')
