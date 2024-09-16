def dfs(level, cnt, cur_sum):
    # 기저 조건
    # 1. 현재 까지의 합이 100을 넘어가면
    if cur_sum > 100:
        return

    # 2. 7명 이상 선택한 경우
    if cnt > 7:
        return

    if level == N:
        if cnt == 7 and cur_sum == 100:
            for i in range(N):
                if visited[i]:
                    print(arr[i])
            exit()
    else:
        visited[level] = 1
        dfs(level+1, cnt + 1, cur_sum + arr[level])
        visited[level] = 0
        dfs(level+1, cnt, cur_sum)
N = 9
arr = [int(input()) for _ in range(N)]
arr.sort()
visited = [0] * N
dfs(0,0,0)
