## 꿀팁 - 비트 연산이 가장 빠름!


# 1

num1, num2 = 10, 5

if num1 & 1:    # num % 2 == 1과 같다
    print('홀수')
else:
    print('짝수')
    
if num2 & 1:    # num % 2 == 1과 같다
    print('홀수')
else:
    print('짝수')



# 2
l, r = 0, 100
mid = (l + r) >> 1  # 50
print(mid)
ss = (l + r) << 1 # 200
print(ss)

# 3

flag = 1
print(flag)
# if flag == 1:
#     flag = 0
# else:
#     flag = 1

flag = flag ^ 1 # 위 코드와 같은 결과
print(flag)
flag ^= 1 # 얘도 같음
print(flag)