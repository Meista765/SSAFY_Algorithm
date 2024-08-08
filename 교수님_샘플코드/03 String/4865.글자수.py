import sys; sys.stdin = open("4865.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    str1 = input()
    str2 = input()

    # 메모리를 추가적으로 사용해서 쉽게 작성
    cnt = [0] * 128  # ASCII 코드값을 배열의 인덱스로 사용

    for ch in str2:
        cnt[ord(ch)] += 1

    ans = 0
    for ch in str1:
        if ans < cnt[ord(ch)]:
            ans = cnt[ord(ch)]

    print(ans)