T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    max_num = arr[0] # 최대값
    min_num = arr[0] # 최솟값

    for i in range(len(arr)):
        # 최대값 갱신
        if max_num < arr[i]:
            max_num = arr[i]

        # 최솟값 갱신
        if min_num > arr[i]:
            min_num = arr[i]

    result = max_num - min_num

    print(f'#{tc} {result}')