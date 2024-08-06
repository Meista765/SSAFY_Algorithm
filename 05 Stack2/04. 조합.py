# ================================
# 중첩반복문으로 5C3 구현

arr = 'ABCDE'
N, R = len(arr), 3          # 5C3 = 10

for i in range(N - 2):              # 첫 번째 요소 선택
    for j in range(i + 1, N - 1):   # 두 번째 요소 선택
        for k in range(j + 1, N):   # 세 번째 요소 선택
            print(arr[i], arr[j], arr[k])

# ================================
# 재귀

arr = 'ABCDE'
N, R = len(arr), 3
pick = [0] * R    # 선택한 R개 저장

def comb(k, s):   # s: 반복의 시작
    if k == R:
        print(pick)
    else:
        remain = R - (k + 1)
        for i in range(s, N - remain):
            pick[k] = arr[i]
            comb(k + 1, i + 1)

comb(0, 0)