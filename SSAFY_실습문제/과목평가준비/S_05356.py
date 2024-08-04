import sys
sys.stdin = open('input.txt','r')

T = int(input())

for test_case in range(1,T+1):
    arr = [input() for _ in range(5)]
    answer = ''


    for j in range(15):
        for i in range(5):
            if j < len(arr[i]):
                answer += arr[i][j]
    
    print(f'#{test_case} {answer}')