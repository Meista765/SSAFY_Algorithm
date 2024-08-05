import sys
sys.stdin = open('C:/Users/SSAFY/Desktop/git/SSAFY_Algorithm/SWEA/SWEA_12394', 'r')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    str_matrix = [list(input()) for _ in range(N)]








    s = input()
    N = len(s)
    ans = 1

    for i in range(N//2):
        if s[i] != s[N - 1 - i]:
            ans = 0
            break
    print(f'#{tc} {ans}')



def find(arr, M):
    pass