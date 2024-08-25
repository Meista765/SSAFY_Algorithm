# i = 0
#
# while i < 3:
#     print('Hello!')
#     i += 1

# 재귀 => 반복
# def print_hello(i, n):
#     if i == n:
#         print('*' * (i+1))
#     else:
#         print('*' * (i+1))
#         print_hello(i+1, n)
#         print('*' * (i+1))   # 재귀호출 다음으로 나오는 애들은 역순으로 실행
#
# print_hello(0, 3)
# '''
# *
# **
# ***
# ****
# ***
# **
# *
# '''

# def print_hello(i, n):
#     if i == n:
#         global cnt
#         cnt += 1
#
#     else:
#         print_hello(i + 1, n)
#         print_hello(i + 1, n)
#
# cnt = 0
# print_hello(0, 3)
# print(cnt)    # 8

# arr = [10, 20, 30]
# N = len(arr)
# bits = [0] * N
# subset = []

# def backtrack(k, n):
#     if k == n:
#         global cnt
#         cnt += 1
#         # print(cnt, bits)
#         print(subset)
#     else:
#         bits[k] = 1   # 왼쪽으로 가는 건 포함 O
#         subset.append(arr[k])
#         backtrack(k + 1, n)
#         subset.pop()

#         bits[k] = 0   # 오른쪽으로 갈 때는 포함 X
#         backtrack(k + 1, n)

# cnt = 0
# backtrack(0, N)
# print(cnt)

# arr = [10, 20, 30]
# N = len(arr)
# bits = [0] * N
#
# for i0 in range(2):
#     for i1 in range(2):
#         for i2 in range(2):
#             print(i0, i1, i2)
#
# def backtrack(k, n, cnt_1, cnt_0):
#     if k == n:
#         print(bits, cnt_1, cnt_0)
#     else:
#         # for i in range(2):
#         #     bits[k] = i
#         #     backtrack(k+1, n)
#
#         bits[k] = 0
#         backtrack(k + 1, cnt_1, cnt_0 +1)
#
#         bits[k] = 1
#         backtrack(k + 1, n, cnt_1+1, cnt_0)
#
# backtrack(0, N, 0, 0)

# ============================================================
# 교환을 통한 순열 생성
# 1. 반복문
# arr = ['A', 'B', 'C', 'D']
# N = len(arr)

# for i in range(0, N):
#     arr[0], arr[i] = arr[i], arr[0]
#     print(arr)
#     '''
#     ['A', 'B', 'C', 'D']
#     ['B', 'A', 'C', 'D']
#     ['C', 'A', 'B', 'D']
#     ['D', 'A', 'B', 'C']
#     '''
#     '''
#     이전에 값을 바꾼 것을 또 사용해서 바꾸기에
#     ['A', 'B', 'C', 'D']
#     ['B', 'A', 'C', 'D']
#     ['C', 'B', 'A', 'D']
#     ['D', 'B', 'C', 'A']
#     가 아닌 위와 같은 결과가 나오게 되는 것
#     따라서 예상한 결과처럼 나오게 하려만 다시 값을 바꾸는 과정 필요
#     '''
# for i in range(0, N):
#     arr[0], arr[i] = arr[i], arr[0]
#     #======================================
#     for j in range(1, N):
#         arr[0], arr[j] = arr[j], arr[0]
#         print(arr)
#         arr[0], arr[j] = arr[j], arr[0]
#     # ======================================
#     arr[0], arr[j] = arr[j], arr[0]
#
#     '''
#     ['B', 'A', 'C', 'D']
#     ['C', 'B', 'A', 'D']
#     ['D', 'B', 'C', 'A']
#     ['D', 'B', 'C', 'A']
#     ['C', 'D', 'B', 'A']
#     ['A', 'D', 'C', 'B']
#     ['D', 'C', 'A', 'B']
#     ['A', 'D', 'C', 'B']
#     ['B', 'D', 'A', 'C']
#     ['D', 'C', 'A', 'B']
#     ['A', 'D', 'C', 'B']
#     ['B', 'D', 'A', 'C']
#     '''

# for i in range(0, N):
#     arr[0], arr[i] = arr[i], arr[0]
#     #======================================
#     for j in range(1, N):
#         arr[1], arr[j] = arr[j], arr[1]
#         # ======================================
#         for k in range(2, N):
#             arr[2], arr[k] = arr[k], arr[2]
#             print(arr)
#             arr[2], arr[k] = arr[k], arr[2]
#         # ======================================
#         arr[1], arr[j] = arr[j], arr[1]
#     # ======================================
#     arr[0], arr[j] = arr[j], arr[0]
#
#     '''
#     ['A', 'B', 'C', 'D']
#     ['A', 'B', 'D', 'C']
#     ['A', 'C', 'B', 'D']
#     ['A', 'C', 'D', 'B']
#     ['A', 'D', 'C', 'B']
#     ['A', 'D', 'B', 'C']
#     ['B', 'D', 'C', 'A']
#     ['B', 'D', 'A', 'C']
#     ['B', 'C', 'D', 'A']
#     ['B', 'C', 'A', 'D']
#     ['B', 'A', 'C', 'D']
#     ['B', 'A', 'D', 'C']
#     ['C', 'D', 'A', 'B']
#     ['C', 'D', 'B', 'A']
#     ['C', 'A', 'D', 'B']
#     ['C', 'A', 'B', 'D']
#     ['C', 'B', 'A', 'D']
#     ['C', 'B', 'D', 'A']
#     ['C', 'D', 'A', 'B']
#     ['C', 'D', 'B', 'A']
#     ['C', 'A', 'D', 'B']
#     ['C', 'A', 'B', 'D']
#     ['C', 'B', 'A', 'D']
#     ['C', 'B', 'D', 'A']
#     '''

# 함수로 만들기
# def backtrack(k, n):
#     if k == n:
#         print(arr)
#     else:
#         for i in range(k, N):
#             arr[k], arr[i] = arr[i], arr[k]
#             # ==============================
#             backtrack(k+1, n)
#             # ==============================
#             arr[k], arr[i] = arr[i], arr[k]

# 교환을 통한 방식은
# 다른 별도의 메모리, 정보를 계산하지 않아도 된다는 장점 존재
# =======================================================
# 2.
arr = ['A', 'B', 'C']
N = len(arr)
order = [0] * N    # 순열을 저장
# visit = [0] * N    # 이미 선택된 요소를 표시

# for i in range(N):
#     if visit[i] == 1: continue
#     visit[i] = 1
#     order[0] = arr[i]
#     for j in range(N):
#         if visit[j] == 1: continue
#         visit[j] == 1
#         order[1] == arr[j]
#         for k in range(N):
#             if visit[k] == 1: continue
#             visit[k] = 1
#             order[2] = arr[k]
#             print(order)
#             visit[k] = 0
#         visit[j] = 0
#     visit[i] = 0

# for i in range(N):
#     if arr[i] in order : continue
#     order.append(arr[i])
#
#     for j in range(N):
#         if arr[j] in order : continue
#         order.append(arr[j])
#
#         for k in range(N):
#             if arr[k] in order: continue
#             order.append(arr[k])
#             print(order)
#             order.pop()
#         order.pop()
#     order.pop()

def backtrack(k, n):
    if k == n:
        print(order)

    else:
        for i in range(N):
            if arr[i] in order: continue
            order.append(arr[i])
            backtrack(k+1, n)
            # 재귀호출
            order.pop()

backtrack(0,N)