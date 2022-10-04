import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

# 깊이 우선 탐색 + dp
def dfs(x, y):
  # 목적지에 도착했을 경우 1을 반환
  if x == n-1 and y == m-1:
    return 1
  
  # 방문한 적 있다면 그 위치에서 출발하는 경우의 수를 반환
  # "가는 길이 같은 경우"
  if visited[x][y] != -1:
    return visited[x][y]

  ways = 0
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < n and 0 <= ny < m and data[x][y] > data[nx][ny]:
      ways += dfs(nx, ny)

  visited[x][y] = ways
  return visited[x][y]

n, m = map(int, input().split())
data = [list(map(int,input().split())) for _ in range(n)]
visited = [list([-1] * m) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(dfs(0, 0))