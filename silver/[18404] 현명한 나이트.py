# 2023/02/06 BFS
# https://www.acmicpc.net/problem/18404
from collections import deque
import sys
input = sys.stdin.readline
dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

def bfs(x, y):
  visited = [[0] * N for _ in range(N)]
  visited[x][y] = 1
  q = deque([(x, y)])
  while q:
    x, y = q.popleft()
    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
        q.append((nx, ny))
        visited[nx][ny] = visited[x][y] + 1
  # 정답 정보 저장
  res = []
  for x, y in horse:
    res.append((visited[x][y] - 1))
  return res

N, M = map(int,input().split())
X, Y = map(int,input().split())

# 말 정보 입력
horse = []
for _ in range(M):
  a, b = map(int,input().split())
  horse.append((a-1, b-1))

# 탐색 시작
res = bfs(X-1, Y-1)

# 정답 출력
print(' '.join(map(str, res)))