# 2023/01/16 BFS
# https://www.acmicpc.net/problem/11967
from collections import deque
import sys
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
  q = deque()
  q.append((0, 0))
  visited = [[False] * N for _ in range(N)] # 방문 기록
  light = [[False] * N for _ in range(N)] # 불켜짐 유무
  visited[0][0] = True
  light[0][0] = True
  res = 1
  for _ in range(len(data[0][0])): # 현재 방에 불을 켤 수 있다면 수행
    a, b = data[0][0].pop()
    if not light[a][b]: # 불 꺼진 곳 키기
      light[a][b] = True
      res += 1
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and light[nx][ny]:
        if data[nx][ny]:
          visited = [[False] * N for _ in range(N)] # 다시 방문해야 한다.
          for _ in range(len(data[nx][ny])):
            a, b = data[nx][ny].pop()
            if not light[a][b]:
              light[a][b] = True
              res += 1
        q.append((nx, ny))
        visited[nx][ny] = True
  return res

if __name__=="__main__":
  N, M = map(int,input().split())
  data = [[[] for _ in range(N)] for _ in range(N)]

  # 스위치 정보 입력
  for i in range(M):
    x, y, a, b = map(int,input().split())
    data[x-1][y-1].append((a-1, b-1))

  # 탐색
  res = bfs()

  # 정답 출력
  print(res)