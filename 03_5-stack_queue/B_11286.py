# 절대값힙
import sys
sys.stdin = open("C:/Users/82108/Downloads/input.txt", "r")
#input = sys.stdin.readline

from queue import PriorityQueue

N = int(input())
myqueue = PriorityQueue()

for i in range(N):
    input_num = int(input())
    if input_num == 0:
        if myqueue.empty():
            print(0)
        else:
            temp = myqueue.get()
            print(str(temp[1]))
    else:
        # 절대값을 기준으로 정렬하고 같으면 음수 우선 정렬하도록 구성
        myqueue.put((abs(input_num), input_num))