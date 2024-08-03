import sys
sys.stdin = open('input.txt','r')
T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    string = input()

    max_one = 0 # 연속된 1의 길이의 최대값
    answer= ''

    # 입력 받은 데이터를 순회하며 1일때 answer에 1 추가 만약 0을 만나면 이전까지 answer의 길이를 확인 후 그 값이 max_one 보다 길면 max_one 갱신
    for i in range(N):
        
        
        if string[i] == '1': 
            answer += '1'
        else:
            if max_one < len(answer):
                max_one = len(answer)
                
            answer = ''
    
    # 마지막이 1로 끝날 경우 다시 한번 확인
           
    if answer:
        if max_one < len(answer):
            max_one = len(answer)
    print(f'#{test_case} {max_one}')

