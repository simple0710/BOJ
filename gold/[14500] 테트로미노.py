import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

# 깊이 우선 탐색으로 검토
def dfs(x, y, tsum, cnt):
  global result
  if cnt == 4:
    result = max(result, tsum)
    return
      
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    # 백트래킹으로 여러 경우 확인
    if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
      visited[nx][ny] = True
      dfs(nx, ny, tsum + graph[nx][ny], cnt + 1)
      visited[nx][ny] = False

# ㅗ, ㅏ,ㅜ, ㅓ 부분 확인  
def check_ah(x, y):
  global result
  # 4방향 확인
  for i in range(4):
    tmp = graph[x][y]
    # 그중 3 영역 지정
    for j in range(3):
      # 012, 123, 230, 301
      t = (i + j) % 4
      nx = x + dx[t]
      ny = y + dy[t]
      # 만약 범위를 벗어나 불가능한 경우
      if not (0 <= nx < n and 0 <= ny < m):
        tmp = 0
        break
      tmp += graph[nx][ny]
    # 최대 값 비교
    result = max(result, tmp)

n, m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False] * m for _ in range(n)]
result = 0
for i in range(n):
  for j in range(m):
    visited[i][j] = True
    dfs(i, j, graph[i][j], 1)
    visited[i][j] = False

    check_ah(i, j)

print(result)