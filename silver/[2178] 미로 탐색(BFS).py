import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  queue = deque()
  queue.append((x, y))
  while queue:
    x, y = queue.popleft()
    # 상, 하, 좌, 우를 확인한다.
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # 범위 안에 들어올 경우 append와 해당 인덱스에 이전 값 + 1을 삽입한다.
      if 0 <= nx < n and 0 <= ny < m and data[nx][ny] == 1:
        queue.append((nx,ny))
        data[nx][ny] = data[x][y] + 1
  return data[n-1][m-1]

n, m = map(int,input().split()) 
data = [list(map(int,input().strip())) for _ in range(n)]
print(bfs(0, 0))