import sys
sys.stdin = open('input.txt','r')

for test_case in range(1,11) :
    tc = int(input())
    P = input()    # pattern
    T = input()    #text
    
    N = len(T)     # text의 길이
    M = len(P)     # pattern의 길이

    cnt = 0        # pattern의 수
    i = 0
    while i+M-1 < N :
        for j in range(M) :
            if P[j] != T[i+j]: # 같지 않으면 멈추고 다음 글자 비교
                break       
        else:
            cnt += 1
            i = i + M-1     # 시작위치를 M만큼 다음 인덱스로 이동
        i += 1              
    print(f'#{tc} {cnt}')