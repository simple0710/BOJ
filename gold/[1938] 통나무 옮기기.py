# 2023/01/29 BFS
# https://www.acmicpc.net/problem/1938
from collections import deque
import sys
input = sys.stdin.readline
dx = [-1, 1, 0 ,0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def bfs(turn, x, y):
  visited = [[[0] * N for _ in range(N)] for _ in range(2)]
  visited[turn][x][y] = 1
  q = deque()
  q.append((turn, x, y))
  while q:
    t, x, y = q.popleft()
    if finish == (t, x, y): # 목적지에 도달한 경우 정답 반환
      return visited[t][x][y] - 1
    # 상하좌우로 움직인다.
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < N:
        if t == 0: # 통나무가 가로로 있는 경우
          left = ny - 1
          right = ny + 1
          # 움직일 수 있고, 해당 공간에 나무가 없으면 움직인다.
          if 0 <= left and right < N and data[nx][ny] == '0' and not visited[t][nx][ny]:
            if data[nx][left] != '1' and data[nx][right] != '1': 
              q.append((t, nx, ny))
              visited[t][nx][ny] = visited[t][x][y] + 1
        if t == 1: # 통나무가 세로로 있는 경우
          up = nx - 1
          down = nx + 1
          # 움직일 수 있고, 해당 공간에 나무가 없으면 움직인다.
          if 0 <= up and down < N and data[nx][ny] == '0' and not visited[t][nx][ny]:
            if data[up][ny] != '1' and data[down][ny] != '1':
              q.append((t, nx, ny))
              visited[t][nx][ny] = visited[t][x][y] + 1
    # 현재 위치에서 회전하기
    nt = (t + 1) % 2 # 0, 1
    if not visited[nt][x][y]:
      flag = True
      for i in range(8): # 3 * 3 구역을 확인한다.
        nx = x + dx[i]
        ny = y + dy[i]
        # 구역 밖이거나, 나무가 있는 경우에는 회전이 불가능 하다.
        if nx < 0 or nx >= N or ny < 0 or ny >= N or data[nx][ny] == '1':
          flag = False
          break
      if flag: # 회전할 수 있는 경우
        visited[nt][x][y] = visited[t][x][y] + 1
        q.append((nt, x, y))
  # 이동 불가능
  return 0

def start_check(i, j, word): # 시작 지점과 도착 지점의 중간 지역을 반환한다.
  for turn, ni, nj in ((0, i, j+1), (1, i+1, j)):
    if 0 <= ni < N and 0 <= nj < N and data[ni][nj] == word:
      value = (turn, ni, nj)
  return value

if __name__=="__main__":
  N = int(input())
  data = [list(input().rstrip()) for _ in range(N)]
  wood = False
  finish = False
  for i in range(N):
    for j in range(N):
      if data[i][j] == 'B':
        if not wood:
          wood = start_check(i, j, 'B') # 중간 지역
        data[i][j] = '0'
      if data[i][j] == 'E':
        if not finish:
          finish = start_check(i, j, 'E') # 중간 지역
        data[i][j] = '0'
  
  # 탐색 시작
  res = bfs(*wood)

  # 정답 출력
  print(res)