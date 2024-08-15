import sys
sys.stdin = open('input.txt')
T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    min_diff = float('inf')
    for i in range(1,N-1):
        for j in range(i+1,N):
            area_1 = sum(arr[:i])
            area_2 = sum(arr[i:j])
            area_3 = sum(arr[j:])
            # print(arr[:i], arr[i:j], arr[j:])
            # print(area_1,area_2,area_3)
            max_val = max(area_1,area_2,area_3)
            min_val = min(area_1,area_2,area_3)
            diff = max_val - min_val


            min_diff = min(min_diff,diff)
    print(f'#{test_case} {min_diff}')