import sys
#input = sys.stdin.readline
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')

N = int(input())  # 숫자의 개수
k = 10000  # 입력 받는 수는 10000보다 작거나 같은 자연수
count_arr = [0] * (k+1)  # 카운팅 배열의 크기는 0부터 10000까지 이므로 10001개

# 카운팅 배열 채우기
for _ in range(N):
    count_arr[int(input())] += 1

# 카운팅 배열을 읽으면서 count_arr[i]가 0이 아니면 해당 값만큼 i 출력
for i in range(k+1):
    if count_arr[i] != 0:
        for _ in range(count_arr[i]):
            print(i)