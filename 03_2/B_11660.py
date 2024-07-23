import sys
sys.stdin = open("C:/Users/SSAFY/Downloads/sample_input.txt", "r")
#input = sys.stdin.readline

table_size, quiz_no = map(int, input().split())
table = [[0] * (table_size+1)] + [[0] + list(map(int, input().split())) for _ in range(table_size)]

prefix_table = [[0 for _ in range(table_size+1)] for _ in range(table_size+1)]  # 구간 합 배열 초기화

# 1행 채우기
for j in range(1, len(prefix_table)):
    prefix_table[1][j] = prefix_table[1][j-1] + table[1][j]
# 1열 채우기
for i in range(1, len(prefix_table)):
    prefix_table[i][1] = prefix_table[i-1][1] + table[i][1]

# 2행, 2열부터 끝까지 채우기
for i in range(2, len(prefix_table)):
    for j in range(2, len(prefix_table)):
        prefix_table[i][j] = prefix_table[i-1][j] + prefix_table[i][j-1] - prefix_table[i-1][j-1] + table[i][j]

# (x1, y1), (x2, y2) 사이 블럭 내 모든 수의 합 구하기 (구간 합 이용)
for _ in range(quiz_no):
    x1, y1, x2, y2 = map(int, input().split())
    print(prefix_table[x2][y2] - prefix_table[x2][y1-1] - prefix_table[x1-1][y2] + prefix_table[x1-1][y1-1])