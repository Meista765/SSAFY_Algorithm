import sys
sys.stdin = open("C:/Users/SSAFY/Downloads/sample_input.txt", "r")
#input = sys.stdin.readline

from collections import deque  # collections 라이브러리의 deque 가져오기
N, L = map(int, input().split())  # N: 주어지는 숫자의 개수, L: i-L+1 번째 수를 찾기 위한 L
num_list = list(map(int, input().split()))  # 숫자 리스트
deq = deque()  # (인덱스, 값) 형태로 원소가 덱에 들어갈 예정

for i in range(N):  # N까지 순회
    while deq and deq[-1][1] > num_list[i]:  # 덱 안에 원소가 있으면서, 그 값이 추후 들어오게될 값보다 크면 반복
        deq.pop()  # 들어오게 될 값보다 큰 원소는 제거
    deq.append((i, num_list[i]))  # 숫자 리스트의 i번째 원소를 맨 오른쪽에 저장 (인덱스, 값)

    # 인덱스 검사
    if deq[0][0] < i - L + 1:  # 가장 왼쪽 원소 인덱스가 범위를 벗어나면
        deq.popleft()  # 가장 왼쪽 원소 제거

    print(deq[0][1], end=' ')  # 가장 왼쪽 원소의 값 출력 (최솟값)