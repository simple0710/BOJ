# 2023/03/11 BFS
# https://www.acmicpc.net/problem/27737
from collections import deque
dx = [-1, 1, 0, 0,]
dy = [0, 0, -1, 1]

def bfs(x, y):
  q = deque()
  q.append((x, y))
  visited[x][y] = True
  cnt = 1
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and data[nx][ny] == 0:
        q.append((nx, ny))
        visited[nx][ny] = True
        cnt += 1
  # 구역의 공간 수 반환
  return cnt

N, M, K = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
area = []
for i in range(N):
  for j in range(N):
    # 해당 공간에 버섯을 심을 수 있는 경우
    if data[i][j] == 0 and not visited[i][j]:
      # 해당 구역의 공간의 수를 area에 추가한다.
      area.append(bfs(i, j))

check = 0
flag = True
if not area: # 심을 수 있는 공간이 없는 경우
  flag = False
while area:
  f = area.pop(0)
  check += f // K # 해당 구역의 공간에 필요한 포자를 심어본다.
  f %= K
  if f % K: # 공간이 남는다면 하나 더 심는다.
    check += 1

if flag and M - check >= 0: # 포자를 심을 수 있는 경우 "POSSIBLE" 출력
  print('POSSIBLE')
  print(M - check)
else: # 포자를 심을 수 없는 경우 "IMPOSSIBLE" 출력
  print('IMPOSSIBLE')