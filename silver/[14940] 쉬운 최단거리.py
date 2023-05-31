# 2023/05/31 BFS
# https://www.acmicpc.net/problem/14940
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # 방문할 수 있는 경우
      if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == -1 and data[nx][ny] != 0:
        q.append((nx, ny))
        visited[nx][ny] = visited[x][y] + 1
  # 정답 출력
  for i in range(N):
    for j in range(M):
      if visited[i][j] == -1 and data[i][j] == 0: # 방문할 수 없는 경우 0 출력
        print(0, end = " ")
      else:
        print(visited[i][j], end = " ") 
    print()

N, M = map(int,input().split())
q = deque()
visited = [[-1] * M for _ in range(N)]
data = []
for i in range(N):
  data.append(list(map(int,input().split())))
  for j in range(M):
    if data[i][j] == 2: # 목표지점
      q.append((i, j))
      visited[i][j] = 0
# 탐색 시작
bfs()