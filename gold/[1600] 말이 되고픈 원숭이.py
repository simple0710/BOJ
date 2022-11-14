# 2022/11/13 BFS
from collections import deque

def bfs():
  q = deque()
  q.append((0, 0, 0))
  dist = [[[False] * N for _ in range(M)] for _ in range(K + 1)]
  dist[0][0][0] = 1
  while q:
    x, y, z = q.popleft()
    # 평범하게 4칸 움직이는 경우
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < M and 0 <= ny < N and not dist[z][nx][ny] and board[nx][ny] != 1:
        dist[z][nx][ny] = dist[z][x][y] + 1
        q.append((nx, ny, z))
    # 말처럼 움직일 수 있는 기회가 있는 경우
    if z + 1 <= K:
      s_nz = z + 1
      for move in s_moves:
        s_nx = x + move[0]
        s_ny = y + move[1]
        if 0 <= s_nx < M and 0 <= s_ny < N and not dist[s_nz][s_nx][s_ny] and board[s_nx][s_ny] != 1:
          dist[s_nz][s_nx][s_ny] = dist[z][x][y] + 1
          q.append((s_nx, s_ny, s_nz))

  res = int(1e9)
  # 목적지 탐색
  for i in range(K+1):
    # 해당 값이 False가 아닌 경우
    if dist[i][M-1][N-1]:
      res = min(res, dist[i][M-1][N-1])
  # 결과값이 변하지 않은 경우 -1 반환
  if res == int(1e9):
    return -1
  # 값이 있는 경우
  else:
    return res - 1

# 정보 입력
K = int(input())
N, M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(M)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
s_moves = [(-1, 2), (-1, -2), (1, 2), (1, -2), (-2, 1), (-2, -1), (2, 1), (2, -1),]

print(bfs())