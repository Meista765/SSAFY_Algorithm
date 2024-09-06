import sys
sys.stdin = open('input.txt')


def dfs(i,j,num):
    if len(num) == 7:
        result.add(num)
        return
    else:
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < 4 and 0 <= nj <4:
                dfs(ni,nj,num+arr[ni][nj])

T = int(input())
for test_case in range(1,T+1):
    arr = [input().split() for _ in range(4)]
    result = set()

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    for i in range(4):
        for j in range(4):
            dfs(i,j,arr[i][j])
    print(f'#{test_case} {len(result)}')


