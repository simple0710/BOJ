# 2023/08/09
# 1. 섬의 번호를 매긴다
# 2. 섬과 섬 사이의 다리를 짓고 정보 저장
# 3. 크루스칼 알고리즘을 이용한 다리의 최소 길이를 구한다.
# 4. 각 섬에 대해 이동할 수 있는 다른 섬의 정보를 배열에 저장한 다음 탐색한다.
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def get_color(x, y):
  q = deque([(x, y)])
  map_data[x][y] = team_flag
  visited[x][y] = True
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < M and map_data[nx][ny] == 1 and not visited[nx][ny]:
        q.append((nx, ny))
        visited[nx][ny] = True
        map_data[nx][ny] = team_flag

def find_road(x, y):
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < N and 0 <= ny < M and map_data[nx][ny] == 0:
      distance = 1
      while 0 <= nx < N and 0 <= ny < M:
        if map_data[nx][ny]:
          if distance - 1 >= 2 and map_data[x][y] != map_data[nx][ny]:
            length_data.append((distance - 1, map_data[x][y], map_data[nx][ny]))
          break
        distance += 1
        nx += dx[i]
        ny += dy[i]

def union(a, b):
  a = find(a)
  b = find(b)
  parent[max(a, b)] = min(a, b)

def find(x):
  if parent[x] != x:
    parent[x] = find(parent[x])
  return parent[x]

def search(v):
  q = deque([v])
  visited[v] = True
  while q:
    v = q.popleft()
    for i in res_check[v]:
      if not visited[i]:
        visited[i] = True
        q.append(i)

N, M = map(int,input().split())
map_data = [list(map(int,input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
team_flag = 1
length_data = []
for i in range(N):
  for j in range(M):
    if map_data[i][j] and not visited[i][j]:
      get_color(i, j)
      team_flag += 1
for i in range(N):
  for j in range(M):
    if map_data[i][j]:
      find_road(i, j)

length_data.sort()

parent = [i for i in range(team_flag)]
res_check = [[] for _ in range(team_flag)]
res = 0
for c, a, b in length_data:
  if find(a) != find(b):
    union(a, b)
    res += c
    res_check[a].append(b)
    res_check[b].append(a)

visited = [False] * team_flag
search(1)
for i in visited[1:]:
  if not i:
    print(-1)
    break
else:
  print(res)