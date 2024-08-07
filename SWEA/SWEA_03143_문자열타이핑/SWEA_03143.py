import sys
sys.stdin = open('C:/Users/SSAFY/Desktop/git/SSAFY_Algorithm/SWEA/SWEA_03143_문자열타이핑/sample_input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    text, pattern = input().split()
    N = len(text)
    M = len(pattern)
    
    # 패턴 발견하면 다음 인덱스로 넘어가게 해야 한다
    cnt = 0
    for i in range(N - M + 1):
        for j in range(M):
            if pattern[j] != text[i + j]:
                break
        else:
            cnt += 1

    number_of_type = N - (M * cnt) + cnt

    print(f'#{tc} {number_of_type}')
