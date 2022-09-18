def dfs(x, y):
  global cnt
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  for i in range(4): # 4방향을 확인한다
    nx = x + dx[i]
    ny = y + dy[i]
    # 범위를 벗어나지 않는 경우
    if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
      graph[nx][ny] = 0
      cnt += 1
      dfs(nx, ny)

n = int(input())
graph = [list(map(int,input())) for _ in range(n)]
total_home = 0
result = list()
# 모든 칸을 확인한다
for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
      cnt = 0
      dfs(i, j)
      total_home += 1 # 모든 집의 수
      if cnt == 0: # 집 구역이 한 칸인 경우 +1을 수행한다.
        cnt += 1
      result.append(cnt)
print(total_home)
result.sort()
for i in result:
  print(i)