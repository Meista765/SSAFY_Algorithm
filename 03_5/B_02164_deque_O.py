import sys
#sys.stdin = open("C:/Users/82108/Downloads/input.txt", "r")
#input = sys.stdin.readline

# deque 라이브러리 사용
from collections import deque
N = int(input())  # 카드 개수
myqueue = deque()

# 큐 채우기
for i in range(1, N+1):
    myqueue.append(i)

while len(myqueue) > 1:  # 카드가 한 장 남을 때까지
    myqueue.popleft()    # 맨 위 카드 버리기
    myqueue.append(myqueue.popleft())  # 맨 위 카드 맨 아래로 보내기

print(myqueue[0])