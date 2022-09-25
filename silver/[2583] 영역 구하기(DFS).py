def dfs(x, y):
  global cnt
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < m and 0 <= ny < n and data[nx][ny] == 0:
      data[nx][ny] = 1
      cnt += 1
      dfs(nx, ny)

m, n, k = map(int, input().split()) # m = 세로, n = 가로, k = 직사각형의 수
data = [list([0] * n) for _ in range(m)]
for _ in range(k):
  # [left_x:right_x], [left_y:right_y] 범위
  left_x, left_y, right_x, right_y = map(int, input().split()) # 가로 세로를 받는다.
  for x in range(left_y, right_y):
    for y in range(left_x, right_x):
      data[x][y] = 1

area = 0
cnt_data = list()
for x in range(m):
  for y in range(n):
    if data[x][y] == 0:
      data[x][y] = 1
      area += 1
      cnt = 1
      dfs(x, y)
      cnt_data.append(cnt)
cnt_data.sort()
print(area)
print(' '.join(map(str, cnt_data)))