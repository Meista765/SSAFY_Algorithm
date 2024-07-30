T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    boxes = list(map(int, input().split()))
    
    max_fall = 0
    for i in range(N - 1):
        shorter_boxes = 0
        for j in range(i + 1, N):
            if boxes[i] <= boxes[j]:
                shorter_boxes += 1
            
        distance_to_fall = (N - i) - shorter_boxes - 1 
        
        if max_fall < distance_to_fall:
            max_fall = distance_to_fall
        
        if max_fall > (N - i):
            break
    
    print(f'#{tc} {max_fall}')
        