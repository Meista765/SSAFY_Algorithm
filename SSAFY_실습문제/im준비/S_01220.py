import sys
sys.stdin = open('input.txt')

# 1: N극, 2: S극, 위: N극, 아래: S극

for test_case in range(1,11):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    cnt = 0
    for j in range(N):
        flag = False
        for i in range(N):
            if arr[i][j] == 1: # N극을 만났을
                flag = True
            elif arr[i][j] == 2 and flag:
                cnt += 1        # 고착상태
                flag = False

    print(f'#{test_case} {cnt}')
