N = 5
arr = [i for i in range(N)]

# 3분할 하기
for i in range(1, N-1):
    for j in range(i + 1, N):
        print(arr[:i], arr[i:j], arr[j:])
