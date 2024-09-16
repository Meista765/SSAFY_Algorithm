import sys
sys.stdin = open('input.txt')

def cal(num1, num2, idx):
    if idx == 0:
        return num1 + num2
    elif idx == 1:
        return num1 - num2
    elif idx ==2:
        return num1 * num2
    else:
        if num1 < 0:
            return -(abs(num1) // num2)
        return num1 // num2



def dfs(level,cur_number):
    global min_val, max_val

    # 종료조건
    if level == N:
        min_val = min(cur_number,min_val)
        max_val = max(cur_number,max_val)
        return

    # 연산자 확인
    for i in range(4):
        if arr[i] == 0:
            continue

        arr[i] -= 1
        dfs(level+1, cal(cur_number, numbers[level], i))
        arr[i] += 1


T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))            # +, -, *, /
    numbers = list(map(int,input().split()))

    min_val = float('inf')
    max_val = float('-inf')

    dfs(1, numbers[0])
    print(f'#{test_case} {max_val - min_val}')