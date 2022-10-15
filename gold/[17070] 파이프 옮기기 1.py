def dfs(data):
  global result
  x, y, z = data
  # 목적지에 도착했을 경우
  if x == n-1 and y == n-1:
    result += 1
    return
  # 대각선인 경우
  if x + 1 < n and y + 1 < n:
    if graph[x + 1][y + 1] == 0 and graph[x][y + 1] == 0 and graph[x + 1][y] == 0:
      dfs((x + 1, y + 1, 2))
  # 대각선, 가로의 경우
  if z == 0 or z == 2:
    if y + 1 < n:
      if graph[x][y + 1] == 0:
        dfs((x, y + 1, 0))
  # 대각선, 세로의 경우
  if z == 1 or z == 2:
    if x + 1 < n:
      if graph[x + 1][y] == 0:
        dfs((x + 1, y, 1))

n = int(input())

graph = [list(map(int,input().split())) for _ in range(n)]

result = 0
dfs((0, 1, 0))
print(result)