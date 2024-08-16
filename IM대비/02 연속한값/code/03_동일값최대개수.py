arr = [0, 0, 2, 2, 1, 3, 2, 2, 2, 1, 1, 1, 1]
N = len(arr)
ans = 0   # 길이 K
cnt = 1   # 초기값 무엇?

for i in range(1, N):
    if arr[i - 1] == arr[i]:
        cnt += 1
        if ans < cnt: ans = cnt
    else:
        # # 최대값 비교
        # if ans < cnt: ans = cnt
        cnt = 1  # <---- 초기값 주의
# 최대값
# if ans < cnt: ans = cnt
print(ans)