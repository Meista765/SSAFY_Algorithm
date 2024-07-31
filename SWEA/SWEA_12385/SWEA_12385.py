import sys
sys.stdin = open("C:/Users/SSAFY/Desktop/스터디/SSAFY_Algorithm/SWEA/SWEA_12385/sample_input.txt", "r")
# input = sys.stdin.readline

T = int(input())

for tc in range(1, T + 1):
    k, n, m = map(int, input().split())
    st_to_charge = list(map(int, input().split()))

    current_idx = 0
    
    visit = 0 
    while True:
        dest_idx = current_idx + k
        if dest_idx >= n:
            break
        # 목표 인덱스부터 탐색
        for i in range(dest_idx, current_idx, -1):
            if i in st_to_charge:
                visit += 1
                current_idx = i
                break
        # 다 탐색해도 없다면 0을 반환하게 for-else
        else:
            visit = 0
            break
    
    print(f'#{tc} {visit}')

