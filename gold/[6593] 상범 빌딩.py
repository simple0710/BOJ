# 2023/01/17 BFS
# https://www.acmicpc.net/problem/6593
from collections import deque
import sys
input = sys.stdin.readline
df = [0, 0, 0, 0, -1, 1]
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]

def bfs(f, x, y):
  visited = [[[False for _ in range(C)] for _ in range(R)] for _ in range(L)] # 열, 행, 층
  visited[f][x][y] = 1
  q = deque()
  q.append((f, x, y))
  while q:
    f, x, y = q.popleft()
    if (f, x, y) == e: # 목적지에 도착한 경우 정답 반환
      return visited[f][x][y] - 1
    for i in range(6):
      nf = f + df[i]
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nf < L and 0 <= nx < R and 0 <= ny < C and not visited[nf][nx][ny]:
        if data[nf][nx][ny] == '.':
          q.append((nf, nx, ny))
          visited[nf][nx][ny] = visited[f][x][y] + 1
  return -1

while True:
  L, R, C = map(int,input().split())
  if L + R + C == 0:
    break
  data = [[] for _ in range(L)]
  for i in range(L):
    for j in range(R):
      data[i].append(list(input().rstrip()))
      for k in range(C):
        if data[i][j][k] == 'S':
          s = (i, j, k)
        if data[i][j][k] == 'E':
          e = (i, j, k)
          data[i][j][k] = '.'
    input()
    
  # 탐색 시작
  res = bfs(*s)

  # 정답 출력
  if res != -1:
    print(f'Escaped in {res} minute(s).')
  else:
    print("Trapped!")