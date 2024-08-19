# 오일러 피 함수 구현하기
import sys
sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")
#input = sys.stdin.readline

'''
1 ~ N 범위에서 N과 서로소인 자연수의 개수 구하기
P[i] = P[i] - P[i] / K
'''

import math

N = int(input())    # 소인수 표현
result = N          # 결괏값

for p in range(2, int(math.sqrt(N))+1):     # 제곱근까지만 진행
    if N % p == 0:                          # p가 소인수인지 확인
        result -= result / p                # 결과값 업데이트
        while N % p == 0:                   # 2^7*11이라면 2^7을 없애고 11만 남김
            N /= p

if N > 1:       # 반복문에서 제곱근까지만 탐색했으므로 1개의 소인수가 누락되는 케이스 처리
    result -= result / N
    
print(int(result))