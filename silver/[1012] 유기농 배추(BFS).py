from collections import deque
import sys
input = sys.stdin.readline

def bfs(x,y):
  queue = deque()
  queue.append((x, y))
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m and data[nx][ny] == 1:
        queue.append((nx, ny))
        data[nx][ny] = 2
  return 1

for _ in range(int(input())):
  m, n, k = map(int,input().split())
  data = [[0 for _ in range(m)] for _ in range(n)]
  
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  for i in range(k):
    a, b = map(int,input().split())
    data[b][a] = 1

  cnt = 0
  for i in range(n):
    for j in range(m):
      if data[i][j] == 1:
        cnt += bfs(i, j)
  print(cnt)