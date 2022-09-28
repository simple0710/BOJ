from collections import deque
import sys
import copy
input = sys.stdin.readline
# 너비 우선 탐색으로 바이러스를 감염 시킨다.
# 남은 안전 구역의 수를 구한다.
def bfs():
  global answer
  new_data = copy.deepcopy(data)
  q = deque()
  # 바이러스에 해당하는 영역을 q에 추가한다.
  for i in range(n):
    for j in range(m):
      if new_data[i][j] == 2:
        q.append((i, j))
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m and new_data[nx][ny] == 0:
        new_data[nx][ny] = 2
        q.append((nx, ny))
  # 안전한 구역의 가장 큰 수를 구한다.
  cnt = 0
  for i in range(n):
    cnt += new_data[i].count(0)
  answer = max(answer, cnt)

# 백트래킹을 이용해 3개의 벽을 세워본다.
# 벽을 다 세우면 바이러스(bfs)로 감염시킨다.
def wall(cnt):
  if cnt == 3:
    bfs()
    return
  for i in range(n):
    for j in range(m):
      if data[i][j] == 0:
        data[i][j] = 1
        wall(cnt+1)
        data[i][j] = 0

n, m = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0
wall(0)
print(answer)