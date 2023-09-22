# 2023/07/23 BFS
# https://www.acmicpc.net/problem/14923
# N * M 미로
# 탈출 : Ex, Ey
# 지팡이 : 1회 벽뚫기
# 탈출 가능한지? 가능하면 가장 빠른 경로
# 이동은 상하좌우
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
  q = deque([(0, Hx, Hy)])
  # 현재 층, 행, 열
  visited = [[[-1] * (M + 1) for _ in range(N + 1)] for _ in range(2)]
  visited[0][Hx][Hy] = 0
  visited[1][Hx][Hy] = 0
  while q:
    f, x, y = q.popleft()
    if (x, y) == (Ex, Ey): # 탈출 위치에 도달한 경우 이동 횟수 반환
      return visited[f][x][y]
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 1 <= nx < N + 1 and 1 <= ny < M + 1: # 1. 범위 안
        # 2. 벽 유무 확인
        if maze[nx][ny]: # 벽인 경우
          if f == 0: # 지팡이를 사용하지 않은 경우 횟수 증가
            floor = 1
          else:  # 지팡이를 사용 했을 경우 넘어감
            continue
        else: # 벽이 아닌 경우 현재층 유지
          floor = f
        if visited[floor][nx][ny] == -1: # 아직 방문하지 않은 칸인 경우
          q.append((floor, nx, ny))
          visited[floor][nx][ny] = visited[f][x][y] + 1
  return -1 # 탈출 위치에 도달하지 못한 경우 -1 반환

N, M = map(int,input().split())
Hx, Hy = map(int,input().split())
Ex, Ey = map(int,input().split())

maze = [[0] * (M + 1)]
maze.extend([[0] + list(map(int,input().split())) for _ in range(N)])

# 탐색 및 정답 출력
print(bfs())