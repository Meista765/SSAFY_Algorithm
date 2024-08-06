import sys; sys.stdin = open('input_01517.txt', 'r', encoding='UTF-8')

def swap(i:int, j:int) -> None:
    global A
    A[i], A[j] = A[j], A[i]

def quick_sort(S, E):
    global A

    if S >= E:
        return
    elif E - S == 1:
        if A[S] > A[E]:
            swap(S, E)
    else:



A = [42, 32, 24, 60, 15, 5, 90, 45]
