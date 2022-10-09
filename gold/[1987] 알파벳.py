# 방법 1 길이만 가져오고 v는 제때 비워둔다.
def dfs(x, y, cnt):
  global result
  result = max(result, cnt)
  v.add(graph[x][y])
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]  
    if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] not in v:
      dfs(nx, ny, cnt + 1)
  v.discard(graph[x][y])
'''
# 방법 2 사실상 순서의 문제
def dfs(x, y, cnt):
  global result
  result = max(result, cnt)
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    # graph[nx][ny] not in v 로 하면 시간초과 발생
    if 0 <= nx < n and 0 <= ny < m and not graph[nx][ny] in v:
      v.add(graph[nx][ny])
      dfs(nx, ny, cnt + 1)
      v.discard(graph[nx][ny])
'''
n, m = map(int,input().split())
graph = [list(map(str,input())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

result = 0
v = set() # set 형식으로 시간 절약

dfs(0, 0, 1) # x, y, v에 담긴 수

print(result)