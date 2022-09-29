from collections import deque
# 너비우선탐색
def bfs():
  q = deque()
  # 미리 1인 경우를 받는다.
  for i in  range(m):
    for j in range(n):
      if data[i][j] == 1:
        q.append((i, j))

  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < m and 0 <= ny < n and data[nx][ny] == 0:
        data[nx][ny] = data[x][y] + 1
        q.append((nx, ny))

n, m = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(m)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

bfs()
cnt = 0
result = 0
# 0이 나오는 경우와 가장 큰 수를 받는다.
for i in data:
  cnt += i.count(0)
  result = max(max(i), result)

# 0이 있다면 -1
if cnt > 0:
  print(-1)
# 아니면 정답 출력, 1부터 시작했기 때문에 -1 수행
else:
  print(result-1)
