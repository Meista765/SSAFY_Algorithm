# 일곱 난쟁이
import sys
sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")
# input = sys.stdin.readline

def DFS(idx, depth, cur_sum):
    global visited
    
    # 가지치기
    if depth > 7:       # 인덱스가 올라가다가, 깊이가 7을 넘어버린 경우
        return
    if cur_sum > 100:   # 내려가던 중 이미 합이 100을 넘어버리면 그 가지는 가망이 없음
        return
    
    # 최대 인덱스에 도달한 경우
    if idx == N:                      
        if depth == 7 and cur_sum == 100:   # 깊이가 7이고 방문표시된 일곱 난쟁이 키의 합이 100이면
            for i in range(N):              # 지금까지 방문표시된 모든 난쟁이들의 키를 출력
                if visited[i]:
                    print(arr[i])
            exit()                          # 찾았으면 프로그램 완전히 종료
        
    # 아직 최대 인덱스까지 가지 못한 경우
    else:                               
        # 현 위치의 값을 포함하고 다음 진행
        visited[idx] = 1
        DFS(idx + 1, depth + 1, cur_sum + arr[idx])
        # 현 위치의 값을 포함하지 않고 다음 진행
        visited[idx] = 0
        DFS(idx + 1, depth, cur_sum)


N = 9
arr = [int(input()) for _ in range(9)]      # 아홉 난쟁이 키
arr.sort()                                  # 나중에 오름차순으로 출력해야하므로 미리 정렬
visited = [0] * N

DFS(0, 0, 0)

#================================================================
# itertools 사용 버전
import sys
from itertools import combinations
input = sys.stdin.readline


heights = [int(input()) for _ in range(9)]      # 아홉 난쟁이 키
for i in combinations(heights, 7):
    if sum(i) == 100:
        result = sorted(list(i))
        for h in result:
            print(h)
