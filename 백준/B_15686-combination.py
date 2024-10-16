import sys
sys.stdin = open('input.txt')

N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

def combination(level,start):
    global min_val

    # 종료조건
    if level == M:
        total_distance = 0
        for i in range(home_cnt):
            check = float('inf')
            r1, c1 = home_location[i]
            for j in pick:
                r2, c2 = chicken_location[j]
                check = min(check, (abs(r1 - r2) + abs(c1 - c2)))
            total_distance += check
            # 가지치기
            if total_distance > min_val:
                return
        if min_val > total_distance:
            min_val = total_distance
        return

    for i in range(start,chicken_cnt):
        pick.append(i)
        combination(level+1, i+1)
        pick.pop()



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

min_val = float('inf')
pick = []

combination(0,0)
print(min_val)