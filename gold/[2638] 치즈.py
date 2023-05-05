# 2023/05/05 Implementation, Simulation, BFS
# https://www.acmicpc.net/problem/2638
from collections import deque
import sys
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
  now_q = deque(now)
  # 이전에 방문했던 위치부터 기존 값을 제거하고 시작
  for x, y in now:
    visited[x][y] = True
    data[x][y] = 0
  now.clear()
  while now_q:
    x, y = now_q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
        if data[nx][ny] == 0: # 0인 경우 이동
          now_q.append((nx, ny))
          visited[nx][ny] = True
        else: # 1인 경우 해당 위치의 값 증가
          data_cnt[nx][ny] += 1
          if data_cnt[nx][ny] >= 2: # 2이상인 경우 다음에 제거
            now.add((nx, ny))

N, M = map(int,input().split())
data = []
data = [list(map(int,input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
data_cnt = [[0] * M for _ in range(N)]
now = set()
now.add((0, 0))
res = 0
while now: # 시작
  res += 1
  bfs()

# 정답 출력
print(res - 1)