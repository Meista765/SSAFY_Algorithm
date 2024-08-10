import sys
input = sys.stdin.readline

# Global variables
S, P = map(int, input().split())
A = input()
count = 0
condition = list(map(int, input().split()))
acgt_to_idx = {
    'A' : 0,
    'C' : 1,
    'G' : 2,
    'T' : 3
}

def validation_check(acgt:list) -> bool:
    global condition
    
    is_ok = True
    for i in range(4):
        if acgt[i] < condition[i]:
            is_ok = False
            break
    
    return is_ok

# 최초 탐색을 위한 변수 선언
window = DNA[0:P]
acgt_count = [
    window.count('A'),
    window.count('C'),
    window.count('G'),
    window.count('T'),
]

if validation_check(acgt_count):
    count += 1

for start in range(1, S-P+1):
    # 윈도우를 수정하기 전에 가장 왼편의 ACGT를 버림
    acgt_count[acgt_to_idx[window[0]]] -= 1
    # 윈도우 수정    
    window = DNA[start:start+P]
    # 윈도우를 수정하고 가장 오른편의 ACGT를 추가함
    acgt_count[acgt_to_idx[window[-1]]] += 1
    # 타당성 검토 후, True이면 count++
    if validation_check(acgt_count):
        count += 1

print(count)