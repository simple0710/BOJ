# 2023/05/15 BFS
# https://www.acmicpc.net/problem/14716
from collections import deque
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, 1, -1, 1, -1]

def bfs(x, y):
  q = deque()
  q.append((x, y))
  visited[x][y] = True
  while q:
    x, y = q.popleft()
    for i in range(8): # 상하좌우, 대각선 확인
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and data[nx][ny] == 1:
        visited[nx][ny] = True
        q.append((nx, ny))

M, N = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(M)]
res = 0
visited = [[False] * N for _ in range(M)]
# 전 범위 탐색
for i in range(M):
  for j in range(N):
    if data[i][j] and not visited[i][j]:
      visited[i][j] = True
      res += 1
      bfs(i, j)
# 정답 출력
print(res)