import sys
#sys.stdin = open("C:/Users/82108/Downloads/input.txt", "r")
#input = sys.stdin.readline

# deque 라이브러리 사용 X (시간 초과)
N = int(input())  # 카드 개수
myqueue = []

# 큐 채우기
for i in range(N, 0, -1):
    myqueue.append(i)

while len(myqueue) > 1:   # 카드가 한 장 남을 때까지
    myqueue.pop()   # 맨 위 카드 버리기
    myqueue = [myqueue.pop()] + myqueue  # 맨 위 카드 맨 아래로 보내기

print(myqueue[0])