# 2023/05/03 BFS
# https://www.acmicpc.net/problem/1303
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
  q = deque()
  q.append((x, y))
  check = 1
  while q:
    x, y = q.popleft()
    for i in range(4): # 4 방향
      nx = x + dx[i]
      ny = y + dy[i]
      # 범위 안, 아군, 확인하지 않은 칸인 경우
      if 0 <= nx < M and 0 <= ny < N and data[x][y] == data[nx][ny] and not visited[nx][ny]:
        q.append((nx, ny))
        visited[nx][ny] = True
        check += 1
  return check ** 2 # 병사 수 N의 제곱 반환

N, M = map(int,input().split())
visited = [[False] * N for _ in range(M)]
data = [list(input()) for _ in range(M)]
res_w, res_b = 0, 0

# 탐색 시작
for i in range(M):
  for j in range(N):
    if not visited[i][j]: # 아직 탐색하지 않은 경우
      visited[i][j] = True
      # 해당 색으로 확인
      check = bfs(i, j)
      if data[i][j] == 'W':
        res_w += check
      else:
        res_b += check
# 정답 출력
print(res_w, res_b)