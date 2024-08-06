data = [69, 10, 30, 2, 16, 8, 31, 22]

# 저장소
H = [0] * 100
last = 0   # 현재 힙에 저장된 자료수, 마지막 노드의 인덱스

def push(item):
    global last
    # 1. 완전 이진 트리 구조를 유지하기 위해 마지막 노드로 추가
    last += 1
    H[last] = item

    # 2. 부모 자식간의 대소 관계를 유지하도록 재조정
    p, c = last//2, last
    while p > 0 and H[p] > H[c]:
        H[p], H[c] = H[c], H[p]
        c = p
        p = c//2

def pop():
    # 루트를 백업해둔다.
    # 1. 완전 이진 트리 유지하기 위해 마지막노드를 루트로 복사
    #    => 마지막노드의 인덱스를 1 감소
    global last
    ret = H[1]
    H[1] = H[last]
    last -= 1

    # 2. 부모/자식간 대소 관계를 재조정
    p, c = 1, 2
    while c <= last:
        # 오른쪽 자식도 관심을 주자
        if c + 1 <= last and H[c] > H[c + 1]:
            c += 1
        if H[p] <= H[c]:
            break
        H[p], H[c] = H[c], H[p]
        p = c
        c = p*2
    return ret

for val in data:
    push(val)

while last:
    print(pop(), end=' ')