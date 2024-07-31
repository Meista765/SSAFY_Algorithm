import sys
sys.stdin = open("C:/Users/SSAFY/Downloads/sample_input.txt", "r")
#input = sys.stdin.readline

N = int(input())  # 입력 받는 수의 개수
arr = [int(input()) for _ in range(N)]

for i in range(N-1):        # 0 ~ N-1
    for j in range(N-1-i):  # 0 ~ N-1-i
        if arr[j] > arr[j+1]:  # 현재 값이 다음 값보다 크면
            arr[j], arr[j+1] = arr[j+1], arr[j]  # 자리 바꾸기

for x in arr:
    print(x)
