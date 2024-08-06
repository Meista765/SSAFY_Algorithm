# 신기한 소수 찾기
import sys
#input = sys.stdin.readline
sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")

N = int(input())   # 자릿수 입력받기

# 소수 판별 함수
def is_prime(str_num):
    num = int(str_num)
    for i in range(2, num//2 + 1):
        if num % i == 0:
            return False
    else:
        return True
    
# 깊이 우선 탐색
def DFS(str_num):
    # 자릿수가 N까지 갈 때까지 살아남았으면 해당 숫자 반환
    if len(str_num) == N:
        print(str_num)
    else:   # 아직 자릿수가 N에 도달하지 못했으면
        for i in range(1, 10, 2):  # 1 3 5 7 9
            if is_prime(str_num + str(i)):   # 기존 숫자에 i를 붙인게 소수이면
                DFS(str_num + str(i))        # DFS 호출

# 일의 자리 소수는 2357 밖에 없기 때문에 이 4개로만 시작
for str_i in '2357':
    DFS(str_i)