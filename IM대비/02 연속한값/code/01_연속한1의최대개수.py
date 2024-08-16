arr = [1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1]
N = len(arr)

ans = 0   # 최대 개수 저장
cnt = 0   # 1의 개수 카운팅
for i in range(N):
    if arr[i] == 1:
        cnt += 1
        if ans < cnt:
            ans = cnt
    else: # arr[i] == 0
        cnt = 0

print(ans)




