arr = '416A676F725974684D2050726F626C656D20536F6C76696E6'


hex_dict = { '0': '0000', '1': '0001', '2': '0010', '3': '0011',
                '4': '0100', '5': '0101', '6': '0110', '7': '0111',
                '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
                'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111' }


# 16진수를 2진수로 변환해서 List(또는 문자열)로 저장
bin_str = ''
for ch in arr:
    bin_str += hex_dict[ch]

print(bin_str)

# =====================================================
hex_dict = {'0': [0, 0, 0, 0], '1': [0, 0, 0, 1], '2': [0, 0, 1, 0], '3': [0, 0, 1, 1],
            '4': [0, 1, 0, 0], '5': [0, 1, 0, 1], '6': [0, 1, 1, 0], '7': [0, 1, 1, 1],
            '8': [1, 0, 0, 0], '9': [1, 0, 0, 1], 'A': [1, 0, 1, 0], 'B': [1, 0, 1, 1],
            'C': [1, 1, 0, 0], 'D': [1, 1, 0, 1], 'E': [1, 1, 1, 0], 'F': [1, 1, 1, 1]}

bin_str = []
for ch in arr:
    bin_str += hex_dict[ch]

print(bin_str)

# =====================================================
bin_str = []
for ch in arr:
    # ch => 정수로 변환
    # if '0' <= ch <= '9':
    #     num = ord(ch) - ord('0')
    # else:
    #     num = 10 + ord(ch) - ord('A')
    num = int(ch, 16)
    bin_str.append(1 if num & 8 else 0) # 8 == 1 << 3
    bin_str.append(1 if num & 4 else 0) # 4 == 1 << 2
    bin_str.append(1 if num & 2 else 0) # 2 == 1 << 1
    bin_str.append(1 if num & 1 else 0) # 1 == 1 < 0
print(bin_str)

# ========================================
res = ''
for i in range(len(arr)):
    tmp = bin(int(arr[i], 16)).lstrip('0b')
    while len(tmp) < 4: tmp = '0' + tmp
    res += tmp
print(res)













