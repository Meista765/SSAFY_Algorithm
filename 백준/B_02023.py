import sys
input = sys.stdin.readline
N = int(input())

# 한자리 소수 2,3,5,7

# 소수 판별 함수
def is_prime(num):
    for i in range(2,int(num**(1/2))+1):
        if num % i ==0:
            return False
    return True

# DFS

def dfs(number):
    if len(str(number)) == N:
        print(number)
    else:
        for i in range(1,10):
            if i % 2 == 0:
                continue
            if is_prime(number*10+i):
                dfs(number*10 + i)

dfs(2)
dfs(3)
dfs(5)
dfs(7)