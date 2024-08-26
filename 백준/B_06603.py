def back_track(k,s):
    if k == 6:
        print(*bits)
    else:
        remain = 6-(k+1)
        for i in range(s, arr[0]-remain):
            bits[k] = arr[i+1]
            back_track(k+1,i+1)







while True:
    arr = list(map(int,input().split()))
    if arr[0] == 0: # 입력의 끝은 0으로 표현
        break
    bits = [0] * 6
    back_track(0,0)
    print()





