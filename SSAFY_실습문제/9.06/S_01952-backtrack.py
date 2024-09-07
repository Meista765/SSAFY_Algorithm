import sys
sys.stdin = open('input.txt')

def backtrack(m,cur_sum):       # m: 월, cur_sum: 현재까지의 합
    global min_price
    # 가지치기(현재까지의 금액이 현재까지의 최소 금액보다 크다면 종료)
    if cur_sum > min_price:
        return

    # 종료조건
    if m > 12:
        min_price = min(min_price, cur_sum)
        return

    # 1일권 구매
    backtrack(m + 1, cur_sum + price[0] * arr[m])
    # 한달권 구매
    backtrack(m + 1, cur_sum + price[1])
    # 3개월권 구매
    backtrack(m + 3, cur_sum + price[2])


T = int(input())
for test_case in range(1,T+1):
    price = list(map(int,input().split()))      # 1일, 1달, 3개월, 12개월
    arr = [0] + list(map(int,input().split()))
    min_price = float('inf')
    backtrack(1,0)  # 1월부터 시작

    min_price = min(min_price, price[3])
    print(f'#{test_case} {min_price}')
