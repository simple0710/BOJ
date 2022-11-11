# 2022/11/11 너비우선탐색
from collections import deque
import sys
input = sys.stdin.readline

# 너비우선탐색
def bfs():
  # 부순 벽의 횟수, 세로, 가로로 방문 기록(이동 횟수)을 저장할 리스트를 생성한다.
  visited = [[[False] * M for _ in range(N)] for _ in range(K + 1)]
  q = deque()
  # 시작지점 정의
  q.append((0, 0, 0))
  visited[0][0][0] = 1
  while q:
    x, y, k = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # 범위 내인 경우
      if 0 <= nx < N and 0 <= ny < M:
        # 깰 수 있는 기회가 있고, 벽을 마주하고, 방문한 적이 없는 경우
        if data[nx][ny] == 1 and k + 1 <= K and not visited[k+1][nx][ny]:
          q.append((nx, ny, k+1))
          visited[k+1][nx][ny] = visited[k][x][y] + 1
        # 평지로 이동
        if data[nx][ny] == 0 and not visited[k][nx][ny]:
          q.append((nx, ny, k))
          visited[k][nx][ny] = visited[k][x][y] + 1

  res = int(1e9)
  # 목적지의 모든 기록을 탐색한다.
  for i in range(K + 1):
    # 해당 값이 False가 아닌 경우 더 적은 값으로 수정한다.
    if visited[i][N-1][M-1]:
      res = min(res, visited[i][N-1][M-1])
  # 해당 값이 바뀐 경우 res를 출력
  if res != int(1e9):
    return res
  # 해당 값이 바뀌지 않은 경우 -1을 출력
  else:
    return -1

# 정보 입력
N, M, K = map(int,input().split())
data = [list(map(int,input().rstrip())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
print(bfs())