T = int(input())

for test_case in range(1,T+1):
    arr = input()
    arr = list(arr)
    N = len(arr)
    answer = 1
    for i in range(N//2):
        if arr[i] != arr[N-1-i]:
            answer = 0
            break
    print(f'#{test_case} {answer}')
