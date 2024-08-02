#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))

    for i in range(N-1):
        for j in range(0,N-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1], arr[j]
    answer = ' '.join(list(map(str,arr)))
    print(f'#{test_case} {answer}')