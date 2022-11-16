# 2022/11/16 BFS
from collections import deque
import sys
input = sys.stdin.readline

def bfs():
  q = deque()
  q.append((0, 0, 0))
  res = 1
  time = True
  while q:
    for _ in range(len(q)):
      x, y, z = q.popleft()
      # 목적지에 도달한 경우
      if x == N - 1 and y == M - 1:
        return res
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and dist[nx][ny] > z:
          # 벽이 아닌 경우
          if data[nx][ny] == 0:
            q.append((nx, ny, z))
            dist[nx][ny] = z
          # # 벽인 경우
          elif z < K:
            # 밤인 경우
            if not time:
              q.append((x, y, z))
            else:
              dist[nx][ny] = z
              q.append((nx, ny, z + 1))
    res += 1
    time = not time
  return -1

N, M, K = map(int,input().split())
data = [list(map(int,input().rstrip())) for _ in range(N)]
dist = [[K + 1] * M for _ in range(N)] # 초기 값으로 벽을 최대로 부수는 횟수를 넣는다.
# 예로 들어  dist[y][x] = 4인 경우 (x, y) 좌표에 벽을 4번 부수고 방문했다는 뜻
# visited[y][x] = 7인 경우(x, y)좌표를 아직 방문하지 않았다는 뜻이다.
dist[0][0] = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 정답 출력
print(bfs())