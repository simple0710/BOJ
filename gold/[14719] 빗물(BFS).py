from collections import deque

# 너비 우선 탐색
def bfs(x, y):
  global total
  q = deque()
  q.append((x, y))
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # graph[0] 과 graph[-1] 에 빈 공간이 있어봐야 물이 고이지 않는다.
      if 0 <= nx < n-1 and 1 <= ny < m-1 and graph[nx][ny] == 0:
        # 좌, 우를 확인해서 벽이 있다면 total += 1
        if (1 in graph[nx][ny+1:]) and (1 in graph[nx][:ny]):
          graph[nx][ny] = 2
          q.append((nx, ny))
          total += 1

# 입력
n, m = map(int,input().split())
data = list(map(int,input().split()))

# 그래프 생성
graph = [list([0] * m) for _ in range(n)]
for i in range(1, n+1):
  for j in range(m):
    if data[j] >= i:
      graph[i-1][j] = 1

total = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 전 영역을 탐색한다.
for i in range(n):
  for j in range(1, m-1):
    if graph[i][j] == 0:
      # 한 영역만 0인 경우 대비
      if (1 in graph[i][j+1:]) and (1 in graph[i][:j]):
        graph[i][j] = 1
        total += 1
        bfs(i, j)
        
print(total)