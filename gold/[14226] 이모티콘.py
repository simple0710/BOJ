# 2022/11/10 너비우선탐색
from collections import deque
import sys
input = sys.stdin.readline

def bfs():
  q = deque()
  # 초기 상태
  q.append((1, 0))
  dist[1][0] = 0
  while q:
    # 화면 이모티콘, 클립보드 이모티콘
    x, y = q.popleft()
    # 이모티콘 클립보드에 복사
    if not dist[x][x]:
      dist[x][x] = dist[x][y] + 1
      q.append((x, x))
    # 클립보드에서 화면으로 이모티콘 붙여넣기
    if x + y <= S and not dist[x + y][y]:
      dist[x + y][y] = dist[x][y] + 1
      q.append((x + y, y))
    # 화면에서 이모티콘 하나 빼기
    if x - 1 >= 0 and not dist[x - 1][y]:
      dist[x - 1][y] = dist[x][y] + 1
      q.append((x - 1, y))
  res = -1
  # 클립보드 복사수에 따른 시간 값을 구한다.
  for i in range(S):
    if dist[S][i]:
      if res == -1 or res > dist[S][i]:
        res = dist[S][i]
  return res

# 정보 입력
S = int(input())
dist = [[False] * (S + 1) for _ in range(S + 1)]
print(bfs())