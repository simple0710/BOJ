# 2022/11/04 너비우선탐색
from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y):
  q = deque()
  q.append((x, y))
  while q:
    x, y = q.popleft()
    visited[x][y] = True
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m:
        # 빙산이 있고, 방문하지 않았다면 이동
        if data[nx][ny] != 0 and not visited[nx][ny]:
          visited[nx][ny] = True
          q.append((nx, ny))
        # 주변에 바다 있다면 해당 cnt에 +1 저장
        elif data[nx][ny] == 0:
          cnt[x][y] += 1

if __name__ == "__main__":
  n, m = map(int,input().split())
  data = [list(map(int,input().split())) for _ in range(n)]
  dx = [-1, 1, 0 ,0]
  dy = [0, 0, -1, 1]
  time = 0
  check = False
  while True:
    visited = [[False] * m for _ in range(n)]
    cnt = [[0] * m for _ in range(n)]
    res = []
    # 빙산 영역 및 녹는 값을 계산해둔다.
    for i in range(n):
      for j in range(m):
        if data[i][j] != 0 and not visited[i][j]:
          res.append(bfs(i, j)) # None 값으로 저장이 된다.
    # 구해둔 값에 대해 계산을 수행한다.
    for i in range(n):
      for j in range(m):
        data[i][j] -= cnt[i][j]
        if data[i][j] < 0:
          data[i][j] = 0
    # 빙산이 다 녹은 경우
    if len(res) == 0:
      break
    # 빙산이 2개 이상인 경우
    if len(res) > 1:
      check = True
      break
    time += 1

  # 빙산이 2개 이상이면 time 출력
  if check:
    print(time)
  # 빙산이 전부 녹은 경우 0 출력
  else:
    print(0)