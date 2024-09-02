import sys
sys.stdin = open('input.txt')

# 암호의 시작 찾기
def find_one():
    for i in range(N):
        for j in range(M-1, -1, -1):
            if arr[i][j] == '1':
                return (i,j)

T = int(input())
for test_case in range(1,T+1):
    N, M = map(int,input().split())
    arr = [input() for _ in range(N)]

    # 암호 사전
    dic = {'0001101':0, '0011001':1, '0010011':2, '0111101':3, '0100011':4,
           '0110001':5, '0101111':6, '0111011':7, '0110111':8, '0001011':9}


    idx = find_one()
    result = ''
    #암호해독
    for s in range(idx[1]-55,idx[1]+1,7):
        key = arr[idx[0]][s:s+7]
        result += str(dic[key])

    # 올바른 암호인지 확인
    tmp = sum(map(int,[result[0],result[2],result[4],result[6]])) * 3 + sum(map(int,[result[1],result[3],result[5],result[7]]))
    if tmp % 10 == 0:
        answer = sum(map(int,list(result)))
    else:
        answer = 0

    print(f'#{test_case} {answer}')