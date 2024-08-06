#=======================================
i = 0
while i < 3:
    print('Hello') # 반복할 작업
    i += 1

# 재귀 호출(1)
def print_hello(i):
    if i == 3:
        return
    else:
        print('Hello')  # 반복할 작업
        print_hello(i + 1)
print_hello(0)
#=======================================
def print_hello(i):
    if i == 3:
        return
    else:
        print('Hello', i)  # 반복할 작업
        print_hello(i + 1)
        print('Bye', i)  # 반복할 작업
print_hello(0)
# ==============================
N = 4
arr = [0] * N
def print_hello(i):
    if i == N:
        print(arr)
        return
    else:
        arr[i] = i + 1
        print_hello(i + 1)
        arr[i] = 0
print_hello(0)
print(arr)
# ==============================
cnt = 0
def print_hello(i):
    if i == 3:
        global cnt
        cnt += 1
    else:
        print_hello(i + 1)
        print_hello(i + 1)

print_hello(0)
print('cnt= ', cnt)

# ==============================
# 최소 값 찾기
arr = [55, 17, 33, 26, 66, 78, 42, 42]

def find_min(s, e):
    if s == e:
        return arr[s]
    else: # s < e
        mid = (s + e) // 2
        l = find_min(s, mid)
        r = find_min(mid + 1, e)
        return l if l < r else r

print(find_min(0, len(arr) - 1))


##### 피보나치 #####
def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)

print(fibo(12)) # 144


##### 팩토리얼 #####
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5)) # 120

#### 배열 순회 ####
arr = [1,2,3,4,5]

def f(i, N, v):
    if i == N:
        return 0
    elif arr[i] == v:
        return i
    else:
        return f(i + 1, N, v)

print(f(0, len(arr), 4)) # 3
print(f(0, len(arr), 6)) # 0