from collections import deque

def bfs(x, y):
  q = deque()
  q.append((x, y))
  while q:
    x, y = q.popleft()
    for step in steps:
      nx = x + step[0]
      ny = y + step[1]
      if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
        visited[nx][ny] = visited[x][y] + 1
        q.append((nx,ny))
  return visited[r2][c2]

# 정보 입력
n = int(input())
visited = [list([0] * n) for _ in range(n)]
r1, c1, r2, c2 = map(int,input().split())

steps = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]

# 너비 우선 탐색 수행
result = bfs(r1, c1)

# 탐색하지 못하면 -1 출력
if result == 0:
  print(-1)
else:
  print(result)