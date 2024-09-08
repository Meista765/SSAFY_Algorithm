import sys
sys.stdin = open('input.txt')


def backtrack(k):
    global ans,A,B
    # # A음식이나 B음식의 재료가 재료의 갯수 /2 보다 커지면 가지치기
    if len(A) > N//2 or len(B) > N//2:
        return

    if k == N:
        if len(A) == N//2:
            A_sum = B_sum = 0
            for i in range(N//2-1):
                for j in range(i+1, N//2):
                    A_sum += arr[A[i]][A[j]] + arr[A[j]][A[i]]
                    B_sum += arr[B[i]][B[j]] + arr[B[j]][B[i]]
            ans = min(ans, abs(A_sum - B_sum))
            return
    A.append(k)
    backtrack(k+1)
    A.pop()
    B.append(k)
    backtrack(k+1)
    B.pop()
T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    ans = float('inf')
    A = []
    B = []
    backtrack(0)
    print(f'#{test_case} {ans}')




