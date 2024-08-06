import sys; sys.stdin = open('1209.txt', 'r')

def find_max_sum(arr, N):
    ans = diag1 = diag2 = 0
    for i in range(100):

        diag1 += arr[i][i]
        diag2 += arr[i][99 - i]

        rsum = csum = 0
        for j in range(100):
            rsum += arr[i][j]
            csum += arr[j][i]

        if ans < rsum: ans = rsum
        if ans < csum: ans = csum

    if ans < diag1: ans = diag1
    if ans < diag2: ans = diag2
    return ans

for tc in range(1, 11):
    N = int(input())
    arr = []
    for i in range(100):
        arr.append(list(map(int, input().split())))

    ans = find_max_sum(arr, N)

    print(f'#{tc} {ans}')