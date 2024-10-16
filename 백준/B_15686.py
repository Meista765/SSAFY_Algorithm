import sys
sys.stdin = open('input.txt')

'''
0: 빈칸, 1: 집 2: 치킨 집
'''

def dfs(level, cnt):
    global min_val
    # 폐업 안 시킬 치킨 집의 수가 M보다 크면 종료
    if cnt > M:
        return

    if level == chicken_cnt:
        if cnt == M:
            total_distance = 0
            for i in range(home_cnt):
                check = float('inf')
                r1, c1 = home_location[i]
                for j in range(chicken_cnt):
                    if pick[j] == 1:
                        r2, c2 = chicken_location[j]
                        check = min(check, (abs(r1 - r2) + abs(c1 - c2)))
                total_distance += check
            if min_val > total_distance:
                min_val = total_distance
        return

    else:
        # 선택 안할 때
        pick[level] = 0
        dfs(level+1, cnt)
        # 선택 할 때
        pick[level] = 1
        dfs(level+1, cnt+1)



N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]


# 집과 치킨 집의 수와 위치를 확인
home_cnt = 0                # 집의 수
home_location = []          # 집의 위치
chicken_cnt = 0             # 치킨집 갯수
chicken_location= []        # 치킨집의 위치
for i in range(N):
    for j in range(N):
        # 치킨 집일 때
        if arr[i][j] == 2:
            chicken_cnt += 1
            chicken_location.append((i,j))

        # 집 일떄
        if arr[i][j] == 1:
            home_cnt += 1
            home_location.append((i,j))

pick = [0] * chicken_cnt
min_val = float('inf')

dfs(0,0)
print(min_val)
