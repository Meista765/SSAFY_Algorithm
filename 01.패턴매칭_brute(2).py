# 염기서열 (ACTG 네개의 물질)
p = "CATTCCCTGCGCCGC"                                                                       # pattern
t = "ATTTGTGCATGTTTGAGCTCATTCCCTGCGCCGCTTTACGTACGAGAAACTGAACGTACCTACGACATTCCCTGCGCCGCCACCCGCTTTTTGAA"      # text

n, m = len(t), len(p)


i = 0
while i < n:
    for j in range(m):
        if p[j] != t[i + j]:
            break
    else:
        print(t[i:i + m])
        i = i + m - 1
    i += 1

