# 델타 연습

## 1. 기준점 4방향(상우하좌)
- 다음 코드에서 예외가 발생하지 않도록 코드를 수정한다.
```python
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

N = 5
arr = [[0] * N for _ in range(N)]

r = 2
c = N-1

for i in range(4):
    nr = r + dr[i]
    nc = c + dc[i]
    arr[r][c] = 1

for line in arr:
    print(*line)
```



## 2. 오른쪽 직선 방향 좌표 생성 

```python
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

N = 7
arr = [[0] * N for _ in range(N)]

r = c = 2

# ------------------------
# 반복문을 이용해서 (r, c)에서 오른쪽 직선 방향의 열값 생성


# ------------------------
for line in arr:
    print(*line)
```

## 3. 네 방향 직선

- 
```python
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

N = 7
arr = [[0] * N for _ in range(N)]

r = c = 2

# ------------------------
# 반복문을 이용해서 (r, c)에서 상하좌우 직선방향 


# ------------------------
for line in arr:
    print(*line)
```

## 4. K 만큼 이동

```python
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

N = 7
arr = [[0] * N for _ in range(N)]

K = 3
r = c = 2

# ------------------------
# 반복문을 이용해서 (r, c)에서 상하좌우 K거리 직선방향


# ------------------------
for line in arr:
    print(*line)
```