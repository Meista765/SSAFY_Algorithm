N = 5
arr = [i for i in range(N)]

# 첫번째 구간의 마지막 인덱스
for i in range(0, N-2 + 1):
    # (0, i) (i + 1, N-1)
    print(arr[:i+1], arr[i+1:N])

print('-----------')
# 두번째 구간의 시작 위치
for i in range(1, N):
    print(arr[:i], arr[i:])

print('-----------')
