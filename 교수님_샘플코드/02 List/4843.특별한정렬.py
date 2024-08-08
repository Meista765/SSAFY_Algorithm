import sys; sys.stdin = open("4843.txt", "r")


for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 선택 정렬
    for i in range(10): # 범위 시작/반복횟수와 관련됨
        idx = i
        if i % 2 == 0:
            for j in range(i + 1, N):
                if arr[idx] < arr[j]:
                    idx = j
        else:
            for j in range(i + 1, N):
                if arr[idx] > arr[j]:
                    idx = j
        arr[i], arr[idx]  = arr[idx], arr[i]

    print(f'#{tc}', end='')
    for i in range(10):
        print(f' {arr[i]}', end='')
    print()
