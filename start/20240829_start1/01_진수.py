"""
10진수 -> 2진수 문장려 변환
"""
num = 46

bin_str = ''
while num:
    # bin_str = str(num % 2) + bin_str
    bin_str = str(num & 1) + bin_str
    # num //= 2
    num >>= 1
print(bin_str)

# =============================================
num = 46

bin_str = ''
while num:
    bin_str = str(num & 1) + bin_str
    num >>= 1
print(bin_str)

# ===============================================
# 변환 해야할 자리수가 정해져 있다면
# => 자리수 만큼 for 문을 활용하는게 좋다.

num = 46
bin_str = ''
# 6자리 출력하기
# 자리수가 정해져 있으므로 앞에서 부터 읽는게 가능한다.
for i in range(5, -1, -1):  # 2^5 -> 2^0 까지 체크
    if num & (1 << i):
        bin_str += '1'
    else:
        bin_str += '0'
print(bin_str)