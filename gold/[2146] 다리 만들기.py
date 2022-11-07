# 2022/10/31 너비우선탐색
from collections import deque
import sys
input = sys.stdin.readline

# 영역을 구분하는 함수
def check_land(x, y, col):
  q = deque()
  q.append((x, y))
  data[x][y] = col
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < n and data[nx][ny] == 1:
        data[nx][ny] = col
        q.append((nx, ny))

# 다리를 만들 수 있는 경우를 계산하는 함수
def check_bridge(x, y, col):
  q = deque()
  q.append((x, y))
  visited = [[0] * n for _ in range(n)]
  while q:
    x, y = q.popleft()
    # 바다가 아니고 내 땅이 아닌 경우 값 반환
    if 0 < data[x][y] < col:
      return visited[x][y] - 1
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # 내 땅이 아니고 방문한 적이 없다면 이동횟수를 1 추가하고 움직인다.
      if 0 <= nx < n and 0 <= ny < n and data[nx][ny] != col and not visited[nx][ny]:
        visited[nx][ny] = visited[x][y] + 1
        q.append((nx, ny))

# 정보 입력
n = int(input())
data = [list(map(int,input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 영역을 구분한다.
col = 2
for i in range(n):
  for j in range(n):
    if data[i][j] == 1:
      check_land(i, j, col)
      col += 1 

# 다리를 짓기
col = 2
ans = list()
for i in range(n):
  for j in range(n):
    # 바다가 아닌 경우 해당 땅에 다리를 짓는다.
    if data[i][j] != 0:
      a = check_bridge(i, j, data[i][j])
      if a != None:
        ans.append(a)

print(min(ans))