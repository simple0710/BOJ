from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y, z):
  q = deque()
  q.append((x, y, z))
  # 방문 정보를 3차원 배열로 확인한다.
  visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
  # 세로, 가로, 부순 기록
  visited[0][0][0] = 1
  while q:
    x, y, z = q.popleft()
    # 목적지에 도달했을 경우 이동 횟수 출력
    if x == n - 1 and y == m - 1:
      return visited[x][y][z]
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m:
        # 다음 칸이 벽이고, 벽을 부술 수 있는 경우
        if graph[nx][ny] == 1 and z == 0:
          visited[nx][ny][1] = visited[x][y][0] + 1
          q.append((nx, ny, 1))
        # 다음 칸이 벽이 아니고, 이동할 수 있는 경우
        elif graph[nx][ny] == 0 and visited[nx][ny][z] == 0:
          visited[nx][ny][z] = visited[x][y][z] + 1
          q.append((nx, ny, z))
  return -1

n, m = map(int,input().split())

graph = [list(map(int, input().rstrip())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0, 0, 0))