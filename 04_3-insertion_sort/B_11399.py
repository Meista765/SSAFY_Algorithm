import sys
input = sys.stdin.readline

N = int(input())  # 사람의 수
P_list = list(map(int, input().split()))  # 각 사람이 돈을 인출하는데 걸리는 시간
S = [0]*N  # 누적합 배열

for cur in range(1, N):
    insert_point = cur
    insert_value = P_list[cur]
    for j in range(cur-1, -1, -1):
        if P_list[j] < P_list[cur]:  # 현 위치보다 탐색 위치의 값이 더 작으면
            insert_point = j + 1   # 탐색 위치 다음 위치에 삽입 예정
            break
    else:
        insert_point = 0           # 끝까지 안나오면 제일 작은거니까 첫 위치에 삽입 예정
    for j in range(cur, insert_point, -1):
        P_list[j] = P_list[j-1]    # 하나씩 위로 올리기
    P_list[insert_point] = insert_value  # 삽입 예정 위치에 현재 위치 값 집어넣기

S[0] = P_list[0]  # 누적합 배열 첫 값은 원본의 첫 값

# 누적합 배열 만들기
for i in range(1, N):
    S[i] = S[i-1] + P_list[i]
    
total_sum = 0

for i in range(N):
    total_sum += S[i]

print(total_sum)