# 2022/11/10 너비우선탐색
from collections import deque

# 너비우선탐색
def bfs():
  dx = [1, 0, -1, 0]
  dy = [0, 1, 0, -1]

  q = deque()
  q.append((0, 0))
  dist[0][0] = 0
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < M:
        # 아직 이동하지 않은 거리인 경우
        if dist[nx][ny] == -1:
          # 벽이 아닌 경우 그냥 이동 후 바로 다시 시행
          if data[nx][ny] == 0:
            dist[nx][ny] = dist[x][y]
            q.appendleft((nx,ny))
          # 벽인 경우 이동 거리에서 +1한 다음 이동
          else:
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))
  # 정답 출력
  return dist[N-1][M-1]

# 정보 입력
M, N = map(int,input().split())
data = [list(map(int,input())) for _ in range(N)]
dist = [[-1] * M for _ in range(N)]
print(bfs())