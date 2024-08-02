import sys
sys.stdin = open('input.txt','r')

T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    answer_list = [0] * 10
    for i in range(10):
        idx = i
        if i % 2 == 0: # 최대
            for j in range(i+1,N):
                if arr[idx] < arr[j]:
                    idx = j

            arr[i],arr[idx] = arr[idx],arr[i]
            answer_list[i] = arr[i]
        else: # 최소
            for j in range(i+1,N):
                if arr[idx] > arr[j]:
                    idx = j
            arr[i],arr[idx] = arr[idx],arr[i]
            answer_list[i] = arr[i]
    print(f'#{test_case}',*answer_list)