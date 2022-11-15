# 2022/11/15 BFS
from collections import deque
import sys
input = sys.stdin.readline

def bfs():
  q = deque()
  # 시작 지점
  q.append((7, 0))
  while q:
    # 겹침 방지용 visited 생성
    visited = [[False] * 8 for _ in range(8)]
    # 가능한 움직임 실행
    for _ in range(len(q)):
      x, y = q.popleft()
      # 목표에 도착한 경우 1 반환
      if x == 0 and y == 7:
        return 1
      # 이동
      for dx, dy in ((0, 0), (-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)):
        nx = x + dx
        ny = y + dy
        if 0 <= nx < 8 and 0 <= ny < 8 and not visited[nx][ny] and data[nx][ny] != '#':
          q.append((nx, ny))
          visited[nx][ny] = True
    # 벽을 아래로 움직임
    for _ in range(len(wall)):
      ### popleft는 맨 위부터 실행 되어 겹칠 우려가 있다. ###
      x, y = wall.pop()
      nx = x + 1
      data[x][y] = '.'
      if nx < 8:
        wall.appendleft((nx, y))
        data[nx][y] = '#'
        if (nx, y) in q:
          q.remove((nx, y))
  return 0

# 정보 입력
data = []
wall = deque()
for i in range(8):
  data.append(list(map(str, input().rstrip())))
  for j in range(8):
    # 벽이면 정보 저장
    if data[i][j] == '#':
      wall.append((i, j))

# 정답 출력
print(bfs())