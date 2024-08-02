

T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))

    max_num = arr[0] + arr[1] #초기값 설정

    for i in range(1,N-1):
        if max_num < arr[i] +arr[i+1]:
            max_num = arr[i] + arr[i+1]
    print(f'#{test_case} {max_num}')