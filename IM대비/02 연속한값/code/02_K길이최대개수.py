arr = [1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1]
N = len(arr)
K = 3
ans = 0   # 길이 K
cnt = 0

for i in range(N):
    if arr[i] == 1:
        cnt += 1
    else:
        if K == cnt:
            ans += 1
        cnt = 0
# 마지막에 한번 더 체크 주기!!!!!!!!
if K == cnt:
    ans += 1
print(ans)
