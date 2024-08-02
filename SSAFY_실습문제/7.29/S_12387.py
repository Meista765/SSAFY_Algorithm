T = int(input())

for test_case in range(1,T+1):
    N, M = map(int, input().split())
    arr = list(map(int,input().split()))

    my_list = [0]*(N-(M-1))

    for i in range(len(my_list)):
        for j in range(0,M):
            my_list[i] += arr[i+j]

    max_num = my_list[0]
    min_num = my_list[0]

    for num in my_list:
        if max_num < num:
            max_num = num
        if min_num > num:
            min_num = num

    print(f'#{test_case} {max_num - min_num}')