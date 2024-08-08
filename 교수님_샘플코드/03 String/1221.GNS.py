import sys; sys.stdin = open('1221.txt', 'r')
       # 0      1      2      3      4
nums = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

T = int(input())
for tc in range(1, T + 1):
    tc_num = input()
    arr = input().split()

    # 빈도수 저장
    cnt = [0] * 10

    # 빈도수 계산
    for num in arr:
        for i in range(10):
            if num == nums[i]:
                cnt[i] += 1
                break

    ans = f'#{tc}'
    for i in range(10):
        ans += f' {nums[i]}' * cnt[i]
    print(ans)
