# 2022/12/04 BFS
# https://www.acmicpc.net/problem/17086
# 상어의 위치를 따로 추가해서 BFS를 수행한 후 그 중간 지점 값을 구하는 방법도 있다.
from collections import deque
import sys
input = sys.stdin.readline

# sx, sy부터 시작해서 상어를 찾는 함수
def bfs(sx, sy):
  global res
  move_x = [-1, 1, 0, 0, -1, -1, 1, 1]
  move_y = [0, 0, -1, 1, -1, 1, -1, 1]
  q = deque()
  q.append((sx, sy))
  visited = [[False] * M for _ in range(N)]
  visited[sx][sy] = 1
  while q:
    x, y = q.popleft()
    # 상어를 만난 경우
    if graph[x][y] == 1:
      res = max(res, visited[x][y] - 1)
      return
    for i in range(8):
      nx = x + move_x[i]
      ny = y + move_y[i]
      if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
        q.append((nx, ny))
        visited[nx][ny] = visited[x][y] + 1

if __name__ == "__main__":
  N, M = map(int, input().split())
  graph = [list(map(int,input().split())) for _ in range(N)]
  res = 0
  # 전 지역을 탐색해서 가장 큰 거리 값을 구한다.
  for i in range(N):
    for j in range(M):
      bfs(i, j)
  # 정답 출력
  print(res)