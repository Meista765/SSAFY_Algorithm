def backtrack(k, n):
    if k == n:
        global cnt
        cnt += 1
    else:
        backtrack(k + 1, n)
        backtrack(k + 1, n)



cnt = 0
backtrack(0, 3)
print(cnt)          # 함수 호출 횟수 ** n   



arr = [10, 20, 30]
N = len(arr)
bit = [0] * N

def backtrack(k, n):
    if k == n:
        print(bit)
    else:
        for i in range(2):
            bit[k] = i
            backtrack(k + 1, n) # N중 포문과 같음!

backtrack(0, N)




def print_hello(i, n):
        if i == n:         
            print('*' * (i+1))
        else:    
            print('*' * (i+1))
            print_hello(i+1, n)
            print('*' * (i+1))

print_hello(0, 5)

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')

def print_hello2(i, n):
        if i == n:         
            print('*' * (i+1))
        else:    
            print('*' * (i+1))
            print_hello2(i+1, n)

print_hello2(0, 5)