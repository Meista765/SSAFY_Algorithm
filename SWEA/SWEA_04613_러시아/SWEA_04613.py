T = int(input())

def count(arr, current_color, color_list):
    # 숫자 세기
    color_dict = {}
    for color in color_list:
        color_dict[color] = 0
    
    for i in range(M):
        color_dict[arr[i]] += 1
    
    max_cnt = 0
    for k, v in color_dict.items():
        if max_cnt < v:
            max_cnt = v
            color = key
        elif max_cnt == v:
            color = current_color
    
    cnt = M - max_cnt
    
    return {
        'count' = cnt,
        'color' = color
    }

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    flag = [list(input()) for _ in range(N)]
    
    painted_boxes = 0
    color_to_paint = ['W', 'B', 'R']
    
    # 첫 줄은 일단 흰색
    current_color = 'W'
    for i in range(M):
        if flag[0][i] != 'W':
            painted_boxes += 1
    
    
    for r in range(1, N):
        arr = flag[r]
    