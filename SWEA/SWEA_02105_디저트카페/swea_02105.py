import sys
sys.stdin = open('sample_input.txt', 'r')

for tc in range(1, int(input()) + 1):
    N = int(input())
    field = [list(map(int, input().split())) for _ in range(N)]
    
    