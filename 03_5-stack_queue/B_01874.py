import sys
sys.stdin = open("C:/Users/SSAFY/Downloads/input.txt", "r")
#input = sys.stdin.readline
            
def stack_arr(arr_len, arr):
    stack = []   # 스택
    answer = []  # +, - 순서대로 저장할 리스트
    num = 1      # 스택에 들어오는 자연수

    for i in range(arr_len):   # 수열의 개수만큼 반복
        if arr[i] >= num:   # 현재 수열 값보다 오름차순 수가 작거나 같으면
            while arr[i] >= num:  # 현재 수열 값에 도달할 때까지 자연수 받기
                stack.append(num)
                num += 1
                answer.append('+')
            stack.pop()  # 현재 수열 값에 도달하면 해당 자연수 pop
            answer.append('-')
        else:   # 현재 수열 값보다 오름차순 수가 크면
            pop_val = stack.pop()
            if pop_val != arr[i]:   # pop된 수가 현재 수열 값이 아니면
                return 'NO'
            else:
                answer.append('-')
    
    return answer

if __name__ == "__main__":
    arr_len = int(input())  # 수열의 개수
    arr = [int(input()) for _ in range(arr_len)]  # 수열
    result = stack_arr(arr_len, arr)
    if result == 'NO':
        print('NO')
    else:
        for plus_minus in result:
            print(plus_minus)