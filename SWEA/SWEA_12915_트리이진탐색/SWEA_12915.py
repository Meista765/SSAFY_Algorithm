import sys
sys.stdin = open('C:/Users/SSAFY/Desktop/git/SSAFY_Algorithm/SWEA/SWEA_12915_트리이진탐색/sample_input.txt', 'r')

def inorder(v):
    global tree
    
    if v == 0: return
    
    inorder(left[v])
    # v는 노드번호
    tree.append(v)
    inorder(right[v])

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    
    left = [0] * (N + 1)
    right = [0] * (N + 1)
    
    for i in range(2, N + 1):
        if i % 2 == 0:
            left[i//2] = i
        else:
            right[i//2] = i
    
    tree = [0]
    
    inorder(1)
    
    print(tree)
    