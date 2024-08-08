import sys; sys.stdin = open('4869.txt', 'r')

for tc in range(1, int(input()) + 1):
    N = int(input())

    def paper(n):
        if n == 10: return 1
        if n == 20: return 3
        return paper(n-10) + paper(n-20)*2

    print(paper(N))
