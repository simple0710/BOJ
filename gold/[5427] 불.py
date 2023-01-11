# 2023/01/10 BFS
# https://www.acmicpc.net/problem/5427
from collections import deque
import sys
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(q, fq):
  t = 0
  # 상근이가 움직일 수 있는 경우 계속 반복
  while q:
    t += 1
    # 불
    for _ in range(len(fq)):
      x, y = fq.popleft()
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < h and 0 <= ny < w and data[nx][ny] == '.':
          fq.append((nx, ny))
          data[nx][ny] = '*'
    # 상근이
    for _ in range(len(q)):
      x, y = q.popleft()
      # 건물의 끝에 도달한 경우 상근이는 탈출할 수 있다.
      if x == 0 or y == 0 or x == h-1 or y == w-1:
        return t
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny]:
          if data[nx][ny] == '.':
            q.append((nx, ny))
            visited[nx][ny] = True
  return -1

for _ in range(int(input())):
  w, h = map(int,input().split())
  fq = deque()
  q = deque()
  visited = [[False] * w for _ in range(h)]
  data = []
  for i in range(h):
    data.append(list(input().rstrip()))
    for j in range(w):
      if data[i][j] == '@':
        q.append((i, j))
        data[i][j] = '.'
        visited[i][j] = True

      elif data[i][j] == '*':
        fq.append((i, j))
  # 탐색
  res = bfs(q, fq)

  # 탈춣한 경우 시간 출력
  if res != -1:
    print(res)
  else:
    print("IMPOSSIBLE")