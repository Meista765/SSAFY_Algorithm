import sys
sys.stdin = open('input.txt')

from collections import deque


T = int(input())

for test_case in range(1,T+1):
    N, M = map(int,input().split())  # N: 오븐 크기 M: 피자의 갯수
    arr = deque([v,i+1] for i,v in enumerate(map(int,input().split()))) # 오븐에 들어갈 피자
    oven = deque()                  # oven
    
    # 처음에 피자 넣어주기
    for _ in range(N):
        pizza = arr.popleft()
        oven.append(pizza)

    while True:
        if len(oven) == 1:      # oven에 피자가 하나 남았다면 
            break               # 멈춤

        for _ in range(N):
            check_pizza = oven.popleft() # 한바퀴 돈 피자 꺼내보기

            if check_pizza[0] //2 ==0:  # 만약 치즈가 다 녹았다면
                if arr:                     # 대기 피자가 있다면
                    new_pizza = arr.popleft()  # 새로운 피자 넣어주기 
                    oven.append(new_pizza)     
                elif len(oven) == 1:    # 만약 대기피자가 없고 oved에 피자가 하나 남았다면 멈추기
                    break
            else:                       # 치즈가 안녹아다면
                check_pizza[0] //= 2
                oven.append(check_pizza)
    answer = oven.popleft()
    print(f'#{test_case} {answer[1]}')

