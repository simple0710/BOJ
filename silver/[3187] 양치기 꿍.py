# 2023/02/18 BFS
# https://www.acmicpc.net/problem/3187
from collections import deque
import sys
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
  q = deque()
  q.append((x, y))
  w = 0
  s = 0
  if data[x][y] == 'k':
    s += 1
  elif data[x][y] == 'v':
    w += 1
  visited[x][y] = True
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < R and 0 <= ny < C and data[nx][ny] != '#' and not visited[nx][ny]:
        if data[nx][ny] == 'k': # 양인 경우
          s += 1
        elif data[nx][ny] == 'v': # 늑대인 경우
          w += 1
        q.append((nx, ny))
        visited[nx][ny] = True
  # 양과 늑대의 값을 비교한 후 값 반환
  if s > w:
    return (s, 0)
  else:
    return (0, w)

R, C = map(int,input().split())
data = [list(input()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]
sheep = 0
wolf = 0
# 탐색 시작
for i in range(R):
  for j in range(C):
    if data[i][j] != '#' and not visited[i][j]:
      x, y = bfs(i, j)
      sheep += x
      wolf += y

# 정답 출력
print(sheep, wolf)