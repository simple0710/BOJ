from collections import deque

# 너비 우선 탐색
def bfs(x, y):
  data[x][y] = 0
  q = deque()
  q.append((x, y))
  while q:
    x, y = q.popleft()
    for step in steps:
      nx = x + step[0]
      ny = y + step[1]
      if 0 <= nx < h and 0 <= ny < w and data[nx][ny] == 1:
        data[nx][ny] = 0
        q.append((nx, ny))

# 갈 수 있는 영역
steps = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, 1), (1, -1)]
while True:
  w, h = map(int,input().split())
  # w와 h가 0일 경우 종료
  if w == 0 and h == 0:
    break
  data = [list(map(int,input().split())) for _ in range(h)]
  cnt = 0
  # 전 영역 탐색
  for i in range(h):
    for j in range(w):
      if data[i][j] == 1:
        cnt += 1
        bfs(i, j)
  print(cnt)