# 2022/12/01 BFS
# https://www.acmicpc.net/problem/16973
from collections import deque
import sys
input = sys.stdin.readline

# BFS
def bfs():
  visited = [[False] * M for _ in range(N)]
  q = deque()
  q.append((Sr-1, Sc-1))
  visited[Sr-1][Sc-1] = 1
  while q:
    x, y = q.popleft()
    # 목적지에 도달한 경우
    if x == Fr - 1 and y == Fc - 1:
      return visited[x][y] - 1 # 정답 반환
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # 주변 영역 체크
      if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
        visited[nx][ny] = visited[x][y] + 1 # 이 위치에 두지 않으면 반복문이 헛돈다.
        if nx + H <= N and ny + W <= M: # 사각형의 크기
          flag = 0
          # 영역 안에 벽이 있는 경우 flag = 1
          for wall_x, wall_y in walls:
            if nx <= wall_x < nx + H and ny <= wall_y < ny + W:
              flag = 1
              break
          # 벽이 없는 경우 좌표를 추가한다.
          if not flag:
            q.append((nx, ny))
  # 불가능한 경우
  return -1

# 정보 입력
N, M = map(int,input().split())
graph = []
walls = []
for i in range(N):
  graph.append(list(map(int,input().split())))
  for j in range(M):
    # 벽 정보 저장
    if graph[i][j] == 1:
      walls.append((i, j))

H, W, Sr, Sc, Fr, Fc = map(int,input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 탐색 및 출력
print(bfs())