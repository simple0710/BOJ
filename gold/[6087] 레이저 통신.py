# 2023/02/13 BFS
# https://www.acmicpc.net/problem/6087
from collections import deque
import sys
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(s, e):
  q = deque()
  visited = [[[False] * M for _ in range(N)] for _ in range(4)] # 들어오는 방향까지 고려한다.
  for i in range(4):
    q.append((i, s[0], s[1]))
    visited[i][s[0]][s[1]] = 1
  while q:
    idx, x, y = q.popleft()
    if (x, y) == e:
      return visited[idx][x][y] - 2 # 시작시 +1, 도착시 +1을 빼준 값을 반환한다.
    for i in range(4):
      nx = x
      ny = y
      while True:
        nx += dx[i]
        ny += dy[i]
        if 0 <= nx < N and 0 <= ny < M and data[nx][ny] != '*': # 범위 내, 벽이 아닌 경우
          # 해당 공간에 방문할 수 있거나, 방문했던 적이 있는데 현재 값 + 1보다 더 큰 경우
          if not visited[i][nx][ny] or visited[i][nx][ny] > visited[idx][x][y] + 1 :
            visited[i][nx][ny] = visited[idx][x][y] + 1
            q.append((i, nx, ny))
        else:
          break
  return

M, N = map(int,input().split())
data = []
s = ""
for i in range(N):
  data.append(list(input().rstrip()))
  for j in range(M):
    if data[i][j] == 'C':
      data[i][j] = '.'
      if not s:
        s = (i, j)
      else:
        e = (i, j)

# 탐색 시작
res = bfs(s, e)

# 정답 출력
print(res)

# # 2022/12/02 BFS
# # https://www.acmicpc.net/problem/6087
# from collections import deque
# import sys
# input = sys.stdin.readline
# INF = int(1e9)

# def bfs(x, y):
#   q = deque()
#   q.append((x, y))
#   visited = [[INF] * N for _ in range(M)]
#   visited[x][y] = -1
#   while q:
#     x, y = q.popleft()
#     # 목적지에 도달한 경우 정답 반환
#     if (x, y) == (fx, fy):
#       return visited[x][y]
#     for i in range(4):
#       nx = x + dx[i]
#       ny = y + dy[i]
#       # 한 반향으로 계속 움직인다.
#       while True:
#         # 범위 안에 있는 경우
#         if 0 <= nx < M and 0 <= ny < N:
#           # 벽이거나 더 많은 유리를 사용하는 경우 break
#           if graph[nx][ny] == '*':
#             break
#           if visited[nx][ny] < visited[x][y] + 1:
#             break
#           q.append((nx, ny))
#           visited[nx][ny] = visited[x][y] + 1
#           # 값 변경
#           nx = nx + dx[i]
#           ny = ny + dy[i]
#         else:
#           break

# if __name__ == "__main__":
#   N, M = map(int,input().split())
#   graph = []
#   C_place = []
#   for i in range(M):
#     graph.append(list(map(str, input())))
#     for j in range(N):
#       if graph[i][j] == 'C':
#         C_place.append((i, j))
#   (sx, sy), (fx, fy) = C_place

#   dx = [-1, 1, 0, 0]
#   dy = [0, 0, -1, 1]

#   # 탐색 및 정답 출력
#   print(bfs(sx, sy))