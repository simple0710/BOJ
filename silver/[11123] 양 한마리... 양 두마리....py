# 2023/07/26 BFS
# https://www.acmicpc.net/problem/11123
from collections import deque
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y):
  grid[x][y] = '.'
  q = deque([(x, y)])
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < H and 0 <= ny < W and grid[nx][ny] == '#': # 양 무리 찾기
        q.append((nx, ny))
        grid[nx][ny] = '.'

for _ in range(int(input())):
  H, W = map(int,input().split())
  grid = [list(input()) for _ in range(H)]
  visited = [[False] * W for _ in range(H)]
  res = 0
  for i in range(H):
    for j in range(W):
      if grid[i][j] == '#': # 양을 발견한 경우
        bfs(i, j) # 탐색 시작
        res += 1
  # 정답 출력
  print(res)