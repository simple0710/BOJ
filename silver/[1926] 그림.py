from collections import deque
def bfs(x, y):
  q = deque()
  q.append((x, y))

  graph[x][y] = 0
  check = 1
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
        graph[nx][ny] = 0
        check += 1
        q.append((nx, ny))
        
  return check

n, m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

total = 0
result = 0
for i in range(n):
  for j in range(m):
    if graph[i][j] == 1:
      total += 1
      result = max(result, bfs(i, j))

print(total)
print(result)