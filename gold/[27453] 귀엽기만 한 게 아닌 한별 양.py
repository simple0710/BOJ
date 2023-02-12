# 2023/02/12 BFS
# https://www.acmicpc.net/problem/27453
from collections import deque
import sys
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
  visited = [[[-1] * M for _ in range(N)] for _ in range(4)] # 들어오는 방향을 고려한다.
  q = deque()
  q.append((s[0], s[1], s, 0)) # x, y, 이전 방문 기록, 이동 횟수
  while q:
    x, y, item, moves = q.popleft()
    if (x, y) == e: # 목적지에 도착한 경우 이동 횟수 반환
      return moves
    item_sum = data[x][y] + data[item[0]][item[1]] # 이전 및 현재 값의 합
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < M and data[nx][ny] != 'X' and (nx, ny) != item: # 벽이 아니고 이전에 방문했던 곳이 아닌 경우
        if visited[i][nx][ny] == -1 or visited[i][nx][ny] > item_sum + data[nx][ny]: # 방문하지 않았거나, 해당 구역의 값보다 낮은 경우
          if item_sum + data[nx][ny] <= K: # K를 넘지 않는 경우
            q.append((nx, ny, (x, y), moves + 1))
            visited[i][nx][ny] = item_sum + data[nx][ny]
  # 불가능한 경우
  return -1

N, M, K = map(int,input().split())
data = []
for i in range(N):
  data.append(list(input().rstrip()))
  for j in range(M):
    if data[i][j].isdecimal():
      data[i][j] = int(data[i][j])
    elif data[i][j] != 'X':
      if data[i][j] == 'H':
        e = (i, j)
      elif data[i][j] == 'S':
        s = (i, j)
      data[i][j] = 0

# 탐색 시작
res = bfs()

# 정답 출력
print(res)