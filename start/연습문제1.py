arr = '0000000111100000011000000111100110000110000111100111100111111001100111'

for i in range(0, len(arr), 7):
    val = 0
    for j in range(i, i + 7):
        if arr[j] == '1':
            val = val*2 + 1
        else:
            val = val*2 + 0
    print(val, end=' ')
print()
# ======================================
for i in range(0, len(arr), 7):
    print(int(arr[i:i+7], 2), end=' ')
print()
# ======================================
for i in range(0, len(arr), 7):
    val = 0
    for j in range(7):
        if arr[i+j] == '1':
            val |= (1 << (6 - j))
    print(val, end=' ')
print()


####### 교수님 연습문제 참고 코드 ####### 
num = 46
# 정수형 자료 => 10진수 문자열
# %, // 연산을 이용
num_str = ''
while num:
    num_str = chr(ord('0') + num % 10) + num_str
    num //= 10
print(num_str)
# ========================================

# 정수형 자료 => 2진수 문자열로 변환
num = 46
num_str = ''
while num:
    num_str = str(num % 2) + num_str
    num //= 2
print(num_str)

# 변환해야할 자리수가 정해졌을 때
# 주어지는 정수값을 N=7자리 2진수 문자열로 변환
num = 46
num_str = ''
for i in range(6, -1, -1): # 2^(N-1) ~ 2^0 의 자리 체크
    if num & (1 << i):
        num_str += '1'
    else:
        num_str += '0'
print(num_str)

# ========================================
# 2진수 문자열 => 정수형 자료
lst = [1, 0, 1, 1, 1, 0]
val = 0
for n in lst:
    val = val*2 + n
print(val)

########## 교수님 연습문제 1 ##########
arr = '0000000111100000011000000111100110000110000111100111100111111001100111'

# arr = '0001101'
for s in range(0, len(arr), 7):
    # s => 7자리 문자열의 모든 시작 위치
    # print(int(arr[s: s + 7], 2), end=' ')
    # range(s, s + 7), arr[s: s + 7]
    num = 0
    for i in range(s, s + 7):
        # print(arr[i], end='')
        if arr[i] == '1':
            num = num * 2 + 1
        else:
            num = num * 2 + 0
    print(num, int(arr[s: s + 7], 2))
print()

## 다른 방식?
arr = '0000000111100000011000000111100110000110000111100111100111111001100111'

for s in range(0, len(arr), 7):
    num = 0
    # 1111000
    for i in range(s, s + 7):
        num = num << 1      # num * 2
        if arr[i] == '1':
            num |= 1        # num = num | 1
    print(num, end=' ')
print()