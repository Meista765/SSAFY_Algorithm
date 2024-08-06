from heapq import heappush, heappop, heapify

data = [69, 10, 30, 2, 16, 8, 31, 22]
H = []
for val in data:
    heappush(H, val)

while H:
    print(heappop(H))

#==========================================
arr = [69, 10, 30, 2, 16, 8, 31, 22]
heapify(arr)
while arr:
    print(heappop(arr), end=' ')

