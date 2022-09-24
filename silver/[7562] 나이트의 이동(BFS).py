from collections import deque
# dfs는 경로가 길어지기 떄문에 이 경우에는 안 좋다고 생각한다.
def bfs(x, y):
  s = deque()
  s.append((x,y))
  # 나이트가 갈 수 있는 모든 경로
  steps = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
  while s:
    x, y = s.popleft()
    for step in steps:
      nx = x + step[0]
      ny = y + step[1]
      # 움직일 수 있는 경우
      if 0 <= nx < length and 0 <= ny < length and visited[nx][ny] == 0:
        s.append((nx,ny))
        visited[nx][ny] = visited[x][y] + 1

for _ in range(int(input())):
  length = int(input())
  visited = [([0] * length) for _ in range(length)]
  x, y = map(int, input().split())
  fx, fy = map(int,input().split())
  cnt = 0
  bfs(x, y)
  # 좌표가 같은 경우
  if x == fx and y == fy:
    print(0)
  else:
    print(visited[fx][fy])

