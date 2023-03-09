# 2023/03/02 DFS
# https://www.acmicpc.net/problem/1245
import sys
input = sys.stdin.readline
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

# 깊이 우선 탐색
def dfs(x, y):
  global flag
  visited[x][y] = True # 해당 구역 방문 처리
  for i in range(8): # 8방향 탐색
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < N and 0 <= ny < M:
      if data[x][y] < data[nx][ny]:  # 더 높은 산봉우리가 있는 경우
        flag = False
      # 방문하지 않은 같은 높이의 산봉우리 탐색
      if not visited[nx][ny] and data[x][y] == data[nx][ny]:
        dfs(nx, ny)
          
N, M = map(int,input().split())
data = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
res = 0
for i in range(N):
  for j in range(M):
    # 탐색하지 않은 경우
    if data[i][j] > 0 and not visited[i][j]:
      flag = True
      dfs(i, j)
      # 산봉우리인 경우 res += 1
      if flag:
        res += 1
# 정답 출력
print(res)
