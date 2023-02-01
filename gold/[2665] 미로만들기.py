# 2023/02/01 BFS
# https://www.acmicpc.net/problem/2665
from collections import deque
import sys
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
  q = deque()
  q.append((0, 0))
  visited = [[int(1e9)] * N for _ in range(N)]
  visited[0][0] = 1
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < N and visited[x][y] < visited[nx][ny]:
        q.append((nx, ny))
        if data[nx][ny] == '1': # 벽이 아닌 경우
          visited[nx][ny] = visited[x][y]
        else: # 벽인 경우
          if visited[x][y] + 1 < visited[nx][ny]:
            q.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1
  # 정답 반환
  return visited[N-1][N-1] - 1 

N = int(input())
data = [list(input().rstrip()) for _ in range(N)]

# 탐색 및 정답 출력
print(bfs())