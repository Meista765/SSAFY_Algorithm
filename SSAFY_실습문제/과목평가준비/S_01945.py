import sys
sys.stdin = open('input.txt','r')

T = int(input())

for test_case in range(1,T+1):
    N = int(input())

    arr = [2,3,5,7,11]
    answer_list = [0] * 5
    
    for i in range(5):
        cnt = 0
        while N % arr[i] == 0: # N이 나누어 떨어지지 않을 때까지
            cnt += 1
            N //= arr[i]
        answer_list[i] = cnt 
           

    print(f'#{test_case}', *answer_list)

