# 2023/05/14 BFS
# https://www.acmicpc.net/problem/13565
from collections import deque
import sys
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
  q = deque()
  visited = [[False] * M for _ in range(N)]
  for i in range(M): # 바깥쪽(위쪽) 정보 입력
    if data[0][i] == 0:
      q.append((0, i))
      visited[0][i] = True
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < M and data[nx][ny] == 0 and not visited[nx][ny]:
        if nx == N - 1: # 안쪽(아래쪽)에 이동 가능한 경우
          print('YES')
          return
        q.append((nx, ny))
        visited[nx][ny] = True
  # 불가능한 경우
  print('NO')

N, M = map(int,input().split())
data = [list(map(int, input().rstrip())) for _ in range(N)]
# 정답 출력
bfs()