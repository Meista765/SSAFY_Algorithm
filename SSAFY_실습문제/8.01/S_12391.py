T = int(input())

def search_count(total_page,search_page):

    cnt = 0
    start = 1
    end = total_page
    while start <= end:
        middle = int((start+end)/2)
        cnt += 1
        if middle == search_page:
            return cnt
        elif middle > search_page:
            end = middle
        else:
            start = middle

    return 1000




for test_case in range(1,T+1):

    total_page, a_search, b_search = map(int,input().split())

    a_cnt = search_count(total_page,a_search)
    b_cnt = search_count(total_page,b_search)

    if a_cnt > b_cnt:
        print(f'#{test_case} B')

    elif a_cnt < b_cnt:
        print(f'#{test_case} A')

    else:
        print(f'#{test_case} 0')

