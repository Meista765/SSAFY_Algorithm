import sys
sys.stdin = open('input.txt')

def check(arr):
    # 가로 검사
    for i in range(9):
        check_list = []
        for j in range(9):
            if arr[i][j] not in check_list:
                check_list.append(arr[i][j])
            else:
                return 0

    # 세로 검사
    for j in range(9):
        check_list = []
        for i in range(9):
            if arr[i][j] not in check_list:
                check_list.append(arr[i][j])
            else:
                return 0

    # 3x3검사
    for i in range(0,9,3):
        for j in range(0,9,3):
            check_list = []
            for k in range(3):
                for l in range(3):
                    if arr[i+k][j+l] not in check_list:
                        check_list.append(arr[i+k][j+l])
                    else:
                        return 0
    return 1




T = int(input())

for test_case in range(1,T+1):
    arr = [list(map(int,input().split())) for _ in range(9)]
    result = check(arr)

    print(f'#{test_case} {result}')

