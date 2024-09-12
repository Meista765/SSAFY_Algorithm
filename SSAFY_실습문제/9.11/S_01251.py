'''
모든 섬에 대해서 어떤 섬에서 그 섬을 제외한 모든 섬을 연결할 때 뜨는 비용을 계산해서 리스트에 담아서 프림 알고리즘을 사용한다.
'''

import sys
sys.stdin = open('input.txt')

def prim(start):
    dist[start] = 0






T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    X = list(map(int,input().split()))
    Y = list(map(int,input().split()))
    E = float(input())

    visited = [0] * N
    dist = [(float('inf'))] * N