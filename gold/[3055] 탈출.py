# 2022/11/01 너비우선탐색
from collections import deque
import sys
input = sys.stdin.readline

# 너비우선 탐색
def start_move():
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  # 고슴도치 기준으로 수행
  while me:
    # 각각 한 사이클을 수행한다.
    # 일단 비에 대해서 먼저 수행한다.
    for _ in range(len(rain)):
      x, y = rain.popleft()
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 비어있는 곳이라면 비를 퍼지게 한다.
        if 0 <= nx < R and 0 <= ny < C and data[nx][ny] == '.':
          data[nx][ny] = '*'
          rain.append((nx, ny))
    # 고슴도치를 움직이게 한다.
    for _ in range(len(me)):
      x, y = me.popleft()
      # 목적지라면 결과값을 반환
      if x == finish_x and y == finish_y:
        return visited[x][y] - 1
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 비어있는 곳이거나 비버 굴인 경우 이동한다.
        if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and (data[nx][ny] == '.' or data[nx][ny] == 'D'):
          visited[nx][ny] = visited[x][y] + 1
          me.append((nx, ny))
  # 고슴도치가 비버 굴로 도착하지 못한 경우
  return 'KAKTUS'

if __name__ == '__main__':
  # 정보 입력(열과 행, 방문 기록)
  R, C = map(int,input().split())
  visited = [[False] * C for _ in range(R)]
  data = list()
  rain = deque()
  me = deque()
  # 특수 지점에 대해서 정보를 기록한다.
  for i in range(R):
    data.append(list(map(str,input().rstrip())))
    for j in range(C):
      if data[i][j] == '*':
        rain.append((i, j))
      elif data[i][j] == 'S':
        me.append((i, j))
        visited[i][j] = 1
        data[i][j] = '.' 
      elif data[i][j] == 'D':
        finish_x, finish_y = i, j
  # 수행 및 출력
  print(start_move())