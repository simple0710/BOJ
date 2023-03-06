# 2023/03/06 BFS, 비트마스킹
# https://www.acmicpc.net/problem/1194
from collections import deque
import sys
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
  visited = [[[False] * M for _ in range(N)] for _ in range(64)]
  q = deque([(0, x, y)])
  visited[0][x][y] = 1
  while q:
    z, x, y = q.popleft()
    # 목적지에 도착한 경우 이동한 거리 반환
    if maze[x][y] == '1':
      return visited[z][x][y] - 1
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # 범위 안이고, 방문하지 않았고, 벽이 아닌 경우
      if 0 <= nx < N and 0 <= ny < M and not visited[z][nx][ny] and maze[nx][ny] != '#':
        if maze[nx][ny].islower(): # 키를 만난 경우
          # 현재 z값과 1을 value('a-f' - 'a')만큼 시프트 연산을 한 값을 or 연산한 값을 nz로 한다.
          nz = z | (1 << (ord(maze[nx][ny]) - ord('a')))
          visited[nz][nx][ny] = visited[z][x][y] + 1
          q.append((nz, nx, ny))
        elif maze[nx][ny].isupper(): # 문을 만난 경우
          # 현재 z값과 1을 value('A-F' - 'A')만큼 시프트 연산을 한 값을 and 했을 때 True인 경우
          if z & (1 << (ord(maze[nx][ny]) - ord('A'))):
            visited[z][nx][ny] = visited[z][x][y] + 1
            q.append((z, nx, ny))
        else: # 빈 칸인 경우
          visited[z][nx][ny] = visited[z][x][y] + 1
          q.append((z, nx, ny))
  # 도착할 수 없는 경우 -1 반환
  return -1
    
N, M = map(int, input().split())
maze = []
for i in range(N):
  maze.append(list(input().rstrip()))
  for j in range(M):
    if maze[i][j] == '0': # 시작 지점 지정
      mx, my = i, j
      maze[i][j] = '.'

# 탐색 시작
res = bfs(mx, my)

# 정답 출력
print(res)