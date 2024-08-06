# 염기서열 (ACTG 네개의 물질)
p = "CATTCCCTGCGCCGC"                                                                       # pattern
t = "ATTTGTGCATGTTTGAGCTCATTCCCTGCGCCGCTTTACGTACGAGAAACTGAACGTACCTACGACATTCCCTGCGCCGCCACCCGCTTTTTGAA"      # text

n, m = len(t), len(p)

# 교재에 포함된 패턴 매칭, 비교시 텍스트 인덱스 i가 증가함
i = j = 0
while i < n:
    if p[j] != t[i]:
        i = i - j
        j = -1

    i, j = i + 1, j + 1
    if j == m:
        print(i - m, t[i - m: i])
        j = 0

# ==================================================
# 비교하는 동안 텍스트 인덱스 i는 시작 위치로 고정
i = 0
while i <= n - m:
    for j in range(m):
        if p[j] != t[i + j]:
            break
    else:
        print(i, t[i:i + m])
        i += m - 1
    i += 1

