# 암호 만들기
import sys
#sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")
#input = sys.stdin.readline

'''
암호: 서로 다른 L개의 알파벳 소문자
- 최소 1개의 모음 (a e i o u)
- 최소 2개의 자음
- 알파벳 오름차순
- 문자의 종류 C가지
'''

def backtrack(idx, pw):
    if len(pw) > L:                     # 암호의 길이가 L을 넘으면
        return                          # 가지치기
    
    if idx == C:                        # 리프 노드에 도달했을 때 
        if len(pw) == L:                # L개의 암호가 완성되면
            # 모음, 자음 개수 세기
            vowel_cnt = 0           # 모음 개수
            consonant_cnt = 0       # 자음 개수
            for ch in pw:
                if ch in 'aeiou':
                    vowel_cnt += 1
                else:
                    consonant_cnt += 1

            # 모음 최소 1개, 자음 최소 2개 만족하면 출력
            if consonant_cnt >= 2 and vowel_cnt >= 1:
                print(pw)
    else:                               # 아직 리프 노드에 도달하지 못했으면
        # 현재 알파벳을 넣는 경우
        backtrack(idx + 1, pw + alpha_lst[idx])
        # 현재 알파벳을 넣지 않는 경우
        backtrack(idx + 1, pw)             


L, C = map(int, input().split())        # L: 알파벳 개수, C: 문자의 가지 수
alpha_lst = sorted(input().split())     # 오름차순으로 출력해야하니 미리 정렬
backtrack(0, '')