import sys
sys.stdin = open('./sample_input.txt', 'r')

N = int(input())

matrix = [list(map(int, input().split())) for _ in range(N)]

max_value = max(map(max, matrix))