from collections import deque
import sys
input = sys.stdin.readline

# 너비 우선 탐색
def bfs(x, y):
  q = deque()
  temp = []
  q.append((x, y))
  temp.append((x, y))
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
        # 두 수의 차가 L보다 크고 R보다 작은 경우
        if L <= abs(graph[nx][ny] - graph[x][y]) <= R:
          visited[nx][ny] = 1
          q.append((nx, ny))
          temp.append((nx, ny))
  return temp

n, L, R = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0
while True:
  visited = [[0] * (n) for _ in range(n)]
  flag = 0
  for i in range(n):
    for j in range(n):
      if visited[i][j] == 0:
        visited[i][j] = 1
        loca = bfs(i, j)
        # 국경선이 열린 경우가 있다면 인구 이동 실시
        if len(loca) > 1:
          flag = 1
          # 각 칸의 수를 연합의 인구수 // 연합의 수로 변경한다.
          number = sum([graph[x][y] for x, y in loca]) // len(loca)
          for x, y in loca:
            graph[x][y] = number
  # 연합을 해체하고, 모든 국경선을 닫는다.
  if flag == 0:
    break
  result += 1

print(result)