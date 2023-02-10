# 2023/02/10 BFS
# https://www.acmicpc.net/problem/3184
from collections import deque
import sys
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
  visited[x][y] = True
  q = deque([(x, y)])
  sheep = 0
  wolf = 0
  while q:
    x, y = q.popleft()
    if data[x][y] == 'v': # 늑대 더하기
      wolf += 1
    elif data[x][y] == 'o': # 양 더하기
      sheep += 1
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and data[nx][ny] != '#':
        visited[nx][ny] = True
        q.append((nx, ny))
  if sheep > wolf: # 양의 수가 더 많은 경우
    return (sheep, 0)
  else: # 늑대의 수가 더 많거나 같은 경우
    return (0, wolf)

R, C = map(int,input().split())
data = [list(input()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]
res_s = 0
res_w = 0

# 탐색 시작
for i in range(R):
  for j in range(C):
    if data[i][j] != '#' and not visited[i][j]:
      check = bfs(i, j)
      res_s += check[0]
      res_w += check[1]

# 정답 출력
print(res_s, res_w)