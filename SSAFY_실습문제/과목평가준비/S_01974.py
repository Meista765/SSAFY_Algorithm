import sys
sys.stdin = open('input.txt','r')

T = int(input())

def check(arr):
    result =1 
    # 행 탐색
    for i in range(9):
        check_list = [0] * 9
        for j in range(9):
            if arr[i][j] not in check_list:
                check_list[j] = arr[i][j]
            else:
                return 0
    

    # 열 탐색
    for j in range(9):
        check_list = [0] * 9
        for i in range(9):
            if arr[i][j] not in check_list:
                check_list[i] = arr[i][j]
            else:
                return 0
   
    # 3 x 3 탐색
    for i in range(0,9,3):
        for j in range(0,9,3):
            check_list = [0] * 9     
            for k in range(3):
                for l in range(3):
                    if arr[i+k][j+l] not in check_list:
                        check_list[arr[i+k][j+l]-1] = arr[i+k][j+l]
                    else:
                        return 0
    
    return result




for test_case in range(1,T+1):
    arr = [list(map(int,input().split())) for _ in range(9)]

    result = check(arr)
  
    print(f'#{test_case} {result}')
    
