# 2023/07/18 BFS
# https://www.acmicpc.net/problem/21736
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
  q = deque([(sx, sy)])
  people = 0
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # 범위 내, 방문하지 않았고, 벽이 아닌 경우
      if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and campus[nx][ny] != 'X':
        visited[nx][ny] = True
        q.append((nx, ny))
        if campus[nx][ny] == 'P': # 사람을 만난 경우
          people += 1
  if people: # 사람을 한 명이상 만난 경우
    return people
  else: # 사람을 만나지 못한 경우
    return 'TT'

N, M = map(int, input().split())
campus = []
visited = [[False] * M for _ in range(N)]
for i in range(N):
  campus.append(list(input()))
  for j in range(M):
    if campus[i][j] == 'I': # 도연이의 위치
      sx, sy = i, j
      visited[sx][sy] = True
# 정답 출력
print(bfs())