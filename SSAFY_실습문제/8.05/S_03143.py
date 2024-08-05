T = int(input())

for test_case in range(1,T+1):
    text, pattern = input().split()
    
    N = len(text) # 전체 텍스트
    M = len(pattern) # 패턴의 길이

    cnt = 0
    i = 0 # t의 인덱스
    
    while i+M-1 < N:
        for j in range(M):
            if pattern[j] != text[i+j]:
                break
        else: 
            cnt += 1
            i = i + M - 1
        i += 1
            
    answer =  N-(M-1)*cnt
    print(f'#{test_case} {answer}')

