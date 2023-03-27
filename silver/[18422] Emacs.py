# 2023/03/27 BFS
# https://www.acmicpc.net/problem/18422
from collections import deque
import sys
input = sys.stdin.readline
dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]

def bfs(x, y):
  q = deque()
  q.append((x, y))
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < M and data[nx][ny] == '*' and not visited[nx][ny]:
        q.append((nx, ny))
        visited[nx][ny] = True
  
N, M = map(int,input().split())
data = [list(input().rstrip()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
res = 0
for i in range(N):
  for j in range(M):
    if data[i][j] == '*' and not visited[i][j]: # 탐색 시작
      visited[i][j] = True
      bfs(i, j)
      res += 1
# 정답 출력
print(res)