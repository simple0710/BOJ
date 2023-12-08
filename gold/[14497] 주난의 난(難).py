# 2023/12/08 0-1 BFS
# https://www.acmicpc.net/problem/14497
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution():
  q = deque([(x1-1, y1-1)])
  visited = [[-1] * M for _ in range(N)]
  visited[x1-1][y1-1] = 0
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == -1:
        visited[nx][ny] = visited[x][y]
        if graph[nx][ny] == '1': # 해당 위치에 친구가 있는 경우 나중에 탐색
          q.append((nx, ny))
          visited[nx][ny] += 1
        elif graph[nx][ny] == '0': # 해당 위치에 아무것도 없는 경우 먼저 탐색
          q.appendleft((nx, ny))
  # 해당 점프에서 한 번 더 점프해야 범인을 찾을 수 있다.
  # 점프 횟수 반환
  return visited[x2-1][y2-1] + 1

def main():
  global N, M, x1, y1, x2, y2, graph
  N, M = map(int,input().split())
  x1, y1, x2, y2 = map(int,input().split())
  graph = [list(input()) for _ in range(N)]
  print(solution()) # 점프 횟수 출력

if __name__ == "__main__":
  main()