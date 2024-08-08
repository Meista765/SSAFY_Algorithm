import sys; sys.stdin = open('1216.txt')

# 조사할 회문의 길이를 작은 값 => 큰값 으로 조사

def find_palindrome(arr, N, M):
    for i in range(N):  # 모든 행
        for j in range(N - M + 1):  # 길이 M인 문자열 모든 시작 위치
            for k in range(M // 2):  # 비교 횟수
                # 시작은 증가시키고 끝은 감소시키면서
                if arr[i][j + k] != arr[i][j + M - k - 1]:
                    break
            else:
                return M

            for k in range(M // 2):
                if arr[j + k][i] != arr[j + M - k - 1][i]:
                    break
            else:
                return M

    return 0

for t in range(1, 11):
    tc_num = input()
    # 하나의 문자열 1차 배열처럼 여겨지니까
    N = 100
    arr = [input() for _ in range(N)]

    ans = 1
    for l in range(2, 101):
        if l - ans > 2:
            break
        ret = find_palindrome(arr, N, l)
        if ret:
            ans = ret

    print(f'#{tc_num} {ans}')