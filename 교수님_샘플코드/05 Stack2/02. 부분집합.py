arr = 'ABCD'; N = len(arr)
bits = [0] * N
# =======================================
# 1단계 반복 구조
for i in range(2):
    bits[0] = i
    for j in range(2):
        bits[1] = j
        for k in range(2):
            bits[2] = k
            print(bits)

# =======================================
# 2단계 재귀구조로 bit 표현 생성
def subset(k, n): # k: 함수호출의 깊이, 노드의 높이, for문의 중첩횟수
    if k == n:
        print(bits, end=' ')
        for i in range(n):
            if bits[i]: print(arr[i], end=' ')
        print()
    else:
        bits[k] = 0
        subset(k + 1, n)
        bits[k] = 1
        subset(k + 1, n)
subset(0, N)

# =======================================
# 3단계
# 전체집합에서 부분집합 생성하고 합계산하기
arr = [1, 2, 1, 2]
N, K = 4, 3
bits = [0] * N
def subset(k, n): # k: 함수호출의 깊이, 노드의 높이, for문의 중첩횟수
    if k == n:
        print(bits, end=' ')
        S = 0
        for i in range(n):
            if bits[i]:
                print(arr[i], end=' ')
                S += arr[i]
        print('==>', S)
    else:
        bits[k] = 0
        subset(k + 1, n)
        bits[k] = 1
        subset(k + 1, n)

subset(0, N)

# =======================================
# 4단계
# 부분집합을 생성하는 과정에서 합을 계산해서 매개변수로 전달하기
arr = [1, 2, 1, 2]
N, K = 4, 3
bits = [0] * N
def subset(k, n, cur_sum): # k: 함수호출의 깊이, 노드의 높이, for문의 중첩횟수
    if k == n:             # cur_sum: 현재까지 선택한 요소의 합
        print(bits, end=' ')
        S = 0
        for i in range(n):
            if bits[i]:
                print(arr[i], end=' ')
                S += arr[i]
        print('==>', S, cur_sum)
    else:
        bits[k] = 0     # k번 요소를 포함하지 않음
        subset(k + 1, n, cur_sum)
        bits[k] = 1     # k번 요소를 포함
        subset(k + 1, n, cur_sum + arr[k])

subset(0, N, 0)

# =======================================
# 5단계
# 가지치기 작용하기
arr = [i for i in range(1, 11)]
N, K = len(arr), 10
cnt = 0
def subset(k, n, cur_sum): # cur_sum: 현재까지 선택한 요소의 합
    if cur_sum > K:
        return

    if k == n:
        global cnt
        if cur_sum == K:
            cnt += 1
    else:
        subset(k + 1, n, cur_sum)
        subset(k + 1, n, cur_sum + arr[k])

subset(0, N, 0); print(cnt)

# =======================================
# 6단계
# 가지치기 작용하기

arr = [i for i in range(1, 11)]
N, K = len(arr), 10
cnt = 0
def subset(k, n, cur_sum, rem_sum): # cur_sum: 현재까지 선택한 요소의 합
    if cur_sum > K:
        return
    if cur_sum == K:
        global cnt
        cnt += 1
        return
    if cur_sum + rem_sum < K:
        return

    if k == n:
        return

    subset(k + 1, n, cur_sum, rem_sum - arr[k])
    subset(k + 1, n, cur_sum + arr[k], rem_sum - arr[k])

subset(0, N, 0, sum(arr)); print(cnt)
