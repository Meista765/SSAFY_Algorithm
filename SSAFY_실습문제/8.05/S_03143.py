T = int(input())

for test_case in range(1,T+1):
    T, P = input().split()
    N = len(T) # 전체 텍스트
    M = len(P) # 패턴의 길이

    cnt = 0
    i = 0 # t의 인덱스
    j = 0 # p의 인덱스
    while j < M and i < N:
        if T[i] == P[j]:
            i =
