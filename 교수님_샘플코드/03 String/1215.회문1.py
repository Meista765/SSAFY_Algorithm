import sys; sys.stdin = open('1215.txt')
def find_palindrome(arr, N):
    for i in range(N//2):
        if arr[i] != arr[N-1-i]:
            return 0
    return 1

N = 8
for tc in range(1, 11):
    M = int(input())
    arr = [input() for _ in range(N)]

    ans = 0
    for r in range(N):
        for s in range(N-M + 1):
            string = ''
            for i in range(s, s + M):
                string += arr[r][i]
            ans += find_palindrome(string, M)

    for c in range(N):
        for s in range(N-M + 1):
            string = ''
            for i in range(s, s + M):
                string += arr[i][c]
            ans += find_palindrome(string, M)

    print(f'#{tc} {ans}')
