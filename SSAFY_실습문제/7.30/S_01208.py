# import sys
# sys.stdin = open("input.txt", "r")
for test_case in range(1):

    dump_count = int(input()) # 덤프카운트
    arr = list(map(int,input().split()))

    for cnt in range(dump_count):
        min_high = arr[0]
        max_high = arr[0]
        max_high_idx = 0
        min_high_idx = 0
        for i in range(1,len(arr)):
            # 최소값 및 그때의 인덱스 찾기
            if min_high > arr[i]:
                min_high = arr[i]
                min_high_idx = i
            # 최대값 및 그때의 인덱스 찾기
            if max_high < arr[i]:
                max_high = arr[i]
                max_high_idx = i
        arr[min_high_idx] += 1
        arr[max_high_idx] -= 1

    final_max_high = arr[0]
    final_min_high = arr[0]

    for j in range(1,len(arr)):
        # 최소값
        if final_min_high > arr[j]:
            final_min_high = arr[j]
        # 최대값
        if final_max_high < arr[j]:
            final_max_high = arr[j]




    print(f'#{test_case} {final_max_high - final_min_high}')