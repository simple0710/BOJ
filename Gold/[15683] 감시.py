# 2023/02/19 구현, Brute Force
# https://www.acmicpc.net/problem/15683
import sys, copy;
input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 감시할 수 있는 공간인지 확인
def question(visited, nx, ny, turn):
  if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] != turn and data[nx][ny] != 6:
    return True
  else:
    return False

def search(idx, visited):
  if idx == len(cctv):
    global res
    p = 0
    # 사각지대의 합 조사
    for i in visited:
      p += i.count(-1)
    # cctv를 지나쳐서 감시한 적이 없는 경우 -1
    for x, y in cctv:
      if visited[x][y] == -1:
        p -= 1
    res = min(res, p - wall)
    return
  x, y = cctv[idx][0], cctv[idx][1]
  # 각 방향에 맞게 범위를 설정한다.
  if data[x][y] == 1:
    for i in range(4):
      new_visited = copy.deepcopy(visited)
      nx = x + dx[i]
      ny = y + dy[i]
      while question(new_visited, nx, ny, i):
        new_visited[nx][ny] = i
        nx += dx[i]
        ny += dy[i]
      search(idx + 1, new_visited)
  elif data[x][y] == 2:
    for i in range(2):
      new_visited = copy.deepcopy(visited)
      nx = x + dx[i]
      ny = y + dy[i]
      while question(new_visited, nx, ny, i):
        new_visited[nx][ny] = i
        nx += dx[i]
        ny += dy[i]
      nx = x + dx[i+2]
      ny = y + dy[i+2]
      while question(new_visited, nx, ny, i + 2):
        new_visited[nx][ny] = i + 2
        nx += dx[i+2]
        ny += dy[i+2]
      search(idx + 1, new_visited)
  elif data[x][y] == 3:
    for i in range(4):
      new_visited = copy.deepcopy(visited)
      nx = x + dx[i]
      ny = y + dy[i]
      while question(new_visited, nx, ny, i):
        new_visited[nx][ny] = i
        nx += dx[i]
        ny += dy[i]
      nx = x + dx[(i+1)%4]
      ny = y + dy[(i+1)%4]
      while question(new_visited, nx, ny, i+1):
        new_visited[nx][ny] = i+1
        nx += dx[(i+1)%4]
        ny += dy[(i+1)%4]
      search(idx + 1, new_visited)
  elif data[x][y] == 4:
    for i in range(4):
      new_visited = copy.deepcopy(visited)
      nx = x + dx[i]
      ny = y + dy[i]
      while question(new_visited, nx, ny, i):
        new_visited[nx][ny] = i
        nx += dx[i]
        ny += dy[i]
      nx = x + dx[(i+1)%4]
      ny = y + dy[(i+1)%4]
      while question(new_visited, nx, ny, i+1):
        new_visited[nx][ny] = (i+1)
        nx += dx[(i+1) % 4]
        ny += dy[(i+1) % 4]
      nx = x + dx[(i+2)%4]
      ny = y + dy[(i+2)%4]
      while question(new_visited, nx, ny, i+2):
        new_visited[nx][ny] = (i+2)
        nx += dx[(i+2)%4]
        ny += dy[(i+2)%4]
      search(idx + 1, new_visited)
  elif data[x][y] == 5:
    new_visited = copy.deepcopy(visited)
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      while question(new_visited, nx, ny, i):
        new_visited[nx][ny] = i
        nx += dx[i]
        ny += dy[i]
    search(idx + 1, new_visited)

N, M = map(int,input().split())
visited=[[-1] * M for _ in range(N)]
res = N * M
cctv = []
data = []
wall = 0
for i in range(N):
  data.append(list(map(int,input().split())))
  for j in range(M):
    if data[i][j]: 
      if data[i][j] != 6:
        cctv.append((i, j))
      else:
        wall += 1

# 감시 시작
search(0, visited)

# 정답 출력
print(res)