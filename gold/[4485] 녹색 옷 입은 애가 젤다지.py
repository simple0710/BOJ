# 2023/01/23 BFS
# https://www.acmicpc.net/problem/4485
from collections import deque
import sys
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
MAX = int(1e9)

def bfs():
  q = deque()
  q.append((0, 0))
  visited[0][0] = cave[0][0] # 시작 값
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < N:
        if (visited[x][y] + cave[nx][ny] < visited[nx][ny]): # 해당 값이 더 작은 경우 해당 위치 추가
          visited[nx][ny] = visited[x][y] + cave[nx][ny]
          q.append((nx, ny))
  return visited[N-1][N-1] # 도착지의 값 반환

t = 1
while True:
  N = int(input())
  if N == 0:
    break
  cave = [list(map(int,input().split())) for  _ in range(N)]
  visited = [[MAX] * N for _ in range(N)]
  print(f'Problem {t}: {bfs()}') # 정답 출력
  t += 1