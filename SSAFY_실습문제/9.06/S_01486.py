import sys
sys.stdin = open('input.txt')

def backtrack(k,cur_sum):
    global answer
    if cur_sum >= B:
        answer = min(answer,cur_sum)
        return

    if k == N:
        return
    else:
        backtrack(k+1,cur_sum+arr[k])
        backtrack(k+1,cur_sum)

T = int(input())
for test_case in range(1,T+1):
    N, B = map(int,input().split())
    arr = list(map(int,input().split()))
    answer = float('inf')
    backtrack(0, 0)
    print(f'#{test_case} {answer-B}')