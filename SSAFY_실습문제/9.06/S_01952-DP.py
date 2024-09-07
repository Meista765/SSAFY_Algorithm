import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1,T+1):
    price = list(map(int,input().split()))      # 1일, 1달, 3개월, 12개월
    arr = [0] + list(map(int,input().split()))
    # dp 초기화
    dp = [0] * 13
    dp[1] = min(price[0] * arr[1], price[1])
    dp[2] = min(dp[1] + price[0] * arr[2], dp[1] + price[1])
    dp[3] = min(dp[2] + price[0] * arr[3], dp[2] + price[1], price[2])
    for i in range(4,13):
        dp[i] = min(dp[i-1] + price[0] * arr[i], dp[i-1] + price[1], dp[i-3] + price[2])

    min_cost = min(dp[12], price[3])
    print(f'#{test_case} {min_cost}')
