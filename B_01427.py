A = list(input())





# 선택 정렬

for i in range(len(A)):
    max_idx = i # 최대값 index
    for j in range(i+1,len(A)):
        if A[max_idx] < A[j]:
            max_idx = j
    A[max_idx], A[i]=A[i],A[max_idx]
for i in range(len(A)):
    print(A[i],end='')