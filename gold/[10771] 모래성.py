# 2022/12/18 BFS
# https://www.acmicpc.net/problem/10711
from collections import deque
import sys
input = sys.stdin.readline

def bfs():
  time = 0
  visited = [[0] * M for _ in range(N)]
  while q:
    x, y = q.popleft()
    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < M:
        # 모래를 깎는다.
        if data[nx][ny] != 0:
          data[nx][ny] -= 1
          # 전부 깎은 경우
          if data[nx][ny] == 0:
            visited[nx][ny] = visited[x][y] + 1
            time = max(time, visited[nx][ny])
            q.append((nx, ny))
  return time

if __name__ == "__main__":
  N, M = map(int,input().split())
  data = []
  q = deque()
  for i in range(N):
    data.append(list(input().rstrip()))
    for j in range(M):
      # 모래를 q에 담는다.
      if data[i][j] == '.':
        data[i][j] = 0
        q.append((i, j))
      else:
        data[i][j] = int(data[i][j])

  dx = [-1, 1, 0, 0, -1, -1, 1, 1]
  dy = [0, 0, -1, 1, -1, 1, -1, 1]

  print(bfs())