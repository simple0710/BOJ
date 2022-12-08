# 2022/12/07 BFS DFS
# https://www.acmicpc.net/problem/1175
from collections import deque
import sys
input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
INF = int(1e9)

# 현재 위치에서 남아있는 모든 C까지의 거리 구하기
def bfs(case, q, visited):
  while q:
    x, y, to = q.popleft()
    if board[x][y] == 'C':
      case.append([visited[x][y][to], x, y, to])
    for i in range(4):
      if i == to:
        continue
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < M and board[nx][ny] != '#' and not visited[nx][ny][i]:
        visited[nx][ny][i] = visited[x][y][to] + 1
        q.append([nx, ny, i])

# 모든 경우에 대해서 해당 점을 시작위치로 하여 dfs 실시
def dfs(dist, sx, sy, to, cnt):
  global res
  if res <= dist:
    return
  # 배달을 완료한 경우 dist 비교  
  if cnt == 2:
    if res > dist:
      res = dist
    return

  visited = [[[0, 0, 0, 0] for _ in range(M)] for _ in range(N)]
  visited[sx][sy][to] = dist
  q = deque([(sx, sy, to)])
  case = []
  bfs(case, q, visited)
  for nd, nsx, nsy, nt in case:
    board[nsx][nsy] = '.'
    dfs(visited[nsx][nsy][nt], nsx, nsy, nt, cnt+1)
    board[nsx][nsy] = 'C'

N, M = map(int,input().rstrip().split())
board = []
for i in range(N):
  board.append(list(input().rstrip()))
  for j in range(M):
    if board[i][j] == 'S':
      board[i][j] = '.'
      sx, sy = i, j
res = INF
for i in range(4):
  dfs(0, sx, sy, i, 0)

# res가 변하지 않으면 -1 출력
if res == INF:
  print(-1)
else:
  print(res)