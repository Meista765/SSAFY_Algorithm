def cross(A,B,N,M):
    # 겹치는 문자의 인덱스 찾기
    # a: A와 B가 겹치는 문자의 A 인덱스, b: A와 B의 겹치는 문자의 B 인덱스
    for i in range(N):
        for j in range(M):
            if A[i] == B[j]:
                return i,j

A, B = input().split()

N = len(A)  # A 문자의 길이
M = len(B)  # B 문자의 길이 +1

# M * N 배열 만들기
arr = [['.'] * N for _ in range(M)]

a,b = cross(A,B,N,M)


# A문자는 j번째 행, B문자는 i번째 열에 들어감

for c in range(N):
    arr[b][c] = A[c]

for r in range(M):
    arr[r][a] = B[r]

for i in range(M):
    print(''.join(arr[i]))


