# 시간 초과
import sys
sys.setrecursionlimit(100000)

def dfs(x, y):
  if x == n - 1 and y == n - 1:
    return 1

  if dp[x][y] != 0:
    return dp[x][y]

  move = [(graph[x][y], 0) , (0, graph[x][y])]
  way = 0
  for i in move:
    nx = x + i[0]
    ny = y + i[1]
    if 0 <= nx < n and 0 <= ny < n and dp[nx][ny] == 0:
      way += dfs(nx, ny)

  dp[x][y] = way
  return dp[x][y]

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

result = 0
print(dfs(0, 0))