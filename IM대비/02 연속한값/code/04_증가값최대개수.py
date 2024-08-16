arr = [4, 5, 6, 1, 2, 3, 1, 2, 5, 6]
N = len(arr)
ans = 0   # 길이 K
cnt = 1   # 초기값 주의

for i in range(1, N):
    if arr[i - 1] < arr[i]:
        cnt += 1
        if ans < cnt:
            ans = cnt
    else:
        cnt = 1  # <---- 초기값 주의

print(ans)