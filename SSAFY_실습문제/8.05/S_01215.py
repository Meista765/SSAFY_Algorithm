import sys
sys.stdin = open('input.txt','r')

for test_case in range(1,11):
    N = int(input())
    arr = [input() for _ in range(8)]
    cnt = 0

    # 행 탐색
    for i in range(8):
        for j in range(8-N+1):
            for k in range(N//2):
                if arr[i][j+k] != arr[i][j+N-1-k]:
                    break
            else:
                cnt +=1
    
    # 열 탐색
    for j in range(8):
        for i in range(8-N+1):
            for k in range(N//2):
                if arr[i+k][j] != arr[i+N-1-k][j]:
                    break
            else:
                cnt += 1
    print(f'#{test_case} {cnt}')




