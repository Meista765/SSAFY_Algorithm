import sys
sys.stdin = open('input.txt')

def pascal(N):
    if N == 1: # N == 1이면 [1]
        return [1]


    else:
        arr = [1] # 맨앞에 [1] 넣어주기
        for i in range(0,N-2): # range -> 전 결과의 마지막 인덱스 전전까지
            arr.append(pascal(N-1)[i]+pascal(N-1)[i+1])
        arr.append(1) # 맨뒤에 [1] 넣어주기
        return arr

T = int(input())

for test_case in range(1,T+1):
    N = int(input())

    print(f'#{test_case}')
    for i in range(1,N+1):
        result = pascal(i)
        print(*result)