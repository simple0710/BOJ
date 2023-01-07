# 2023/01/07 BFS
# https://www.acmicpc.net/problem/4179
from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y, fq):
  visited = [[False] * C for _ in range(R)]
  visited[x][y] = True
  q = deque()
  q.append((x, y))
  t = 0
  while q:
    t += 1
    # 불 퍼지기
    for _ in range(len(fq)):
      x, y = fq.popleft()
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and data[nx][ny] == '.':
          fq.append((nx, ny))
          data[nx][ny] = 'F'
    # 사람 움직이기
    for _ in range(len(q)):
      x, y = q.popleft()
      # 가장자리에 도착한 경우 정답 반환
      if x == R - 1 or y == C - 1 or x == 0 or y == 0:
        return t
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]:
          if data[nx][ny] == '.':
            q.append((nx, ny))
            visited[nx][ny] = True

R, C = map(int,input().split())
data = []
fq = deque()
for i in range(R):
  data.append(list(input().rstrip()))
  for j in range(C):
    if data[i][j] == 'J':
      x, y = i, j
      data[i][j] = '.'
    elif data[i][j] == 'F':
      fq.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 탐색 시작
res = bfs(x, y, fq)

# t 가 반환된 경우 t 출력, 아니면 불가능 출력
if res:
  print(res)
else:
  print('IMPOSSIBLE')