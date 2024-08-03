T = int(input())

for test_case in range(1,T+1):

 
    money = int(input())
    change_money = [50000,10000,5000,1000,500,100,50,10]
    print(f'#{test_case}')
    for i in change_money:
        print(f'{money//i}',end = ' ')
        money = money%i
    print()