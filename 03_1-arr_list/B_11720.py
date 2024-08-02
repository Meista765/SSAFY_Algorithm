N = int(input())  # 숫자 개수 입력
num = input()  # 숫자 N개 공백 없이 입력
numsum = 0

for i in range(N):  # 0부터 N-1까지 loop
    numsum += int(num[i])  # num의 i번째 수를 numsum에 더하기

print(numsum)  # 다 더해진 결과 출력