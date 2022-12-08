# 2022/12/02 BFS
# https://www.acmicpc.net/problem/6087
from collections import deque
import sys
input = sys.stdin.readline
INF = int(1e9)

def bfs(x, y):
  q = deque()
  q.append((x, y))
  visited = [[INF] * N for _ in range(M)]
  visited[x][y] = -1
  while q:
    x, y = q.popleft()
    # 목적지에 도달한 경우 정답 반환
    if (x, y) == (fx, fy):
      return visited[x][y]
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # 한 반향으로 계속 움직인다.
      while True:
        # 범위 안에 있는 경우
        if 0 <= nx < M and 0 <= ny < N:
          # 벽이거나 더 많은 유리를 사용하는 경우 break
          if graph[nx][ny] == '*':
            break
          if visited[nx][ny] < visited[x][y] + 1:
            break
          q.append((nx, ny))
          visited[nx][ny] = visited[x][y] + 1
          # 값 변경
          nx = nx + dx[i]
          ny = ny + dy[i]
        else:
          break

if __name__ == "__main__":
  N, M = map(int,input().split())
  graph = []
  C_place = []
  for i in range(M):
    graph.append(list(map(str, input())))
    for j in range(N):
      if graph[i][j] == 'C':
        C_place.append((i, j))
  (sx, sy), (fx, fy) = C_place

  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]

  # 탐색 및 정답 출력
  print(bfs(sx, sy))