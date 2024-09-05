import sys
sys.stdin = open('./sample_input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    
    V = [0]   # 부피
    C = [0]   # 가치
    
    for _ in range(N):
        v_i, c_i = map(int, input().split())
        V.append(v_i)
        C.append(c_i)
    
    print(V, C)