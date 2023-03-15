# 2023/03/15 Implementation
# https://www.acmicpc.net/problem/23289
from collections import deque
import sys, copy
input = sys.stdin.readline
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def start_controll(x, y, c):
  visited = [[False] * C for _ in range(R)]
  if 0 <= x + dx[c] < R and 0 <= y + dy[c] < C:
    q = deque([(x + dx[c], y + dy[c], 5)])
    while q:
      x, y, v = q.popleft()
      data[x][y] += v
      if v > 1:
        nx = x + dx[c]
        ny = y + dy[c]
        if 0 <= nx < R and 0 <= ny < C:
          if not wall[c][x][y] and not visited[nx][ny]:
            q.append((nx, ny, v - 1))
            visited[nx][ny] = True
          if c >= 2: 
            if 0 <= y - 1:
              if not wall[1][x][y] and not wall[c][x][y-1] and not visited[nx][y-1]:
                q.append((nx, y-1, v-1))
                visited[nx][y-1] = True
            if y + 1 < C:
              if not wall[0][x][y] and not wall[c][x][y+1] and not visited[nx][y+1]:
                q.append((nx, y+1, v-1))
                visited[nx][y+1] = True
          else:
              if 0 <= x - 1:
                if not wall[2][x][y] and not wall[c][x-1][y]  and not visited[x-1][ny]:
                  q.append((x-1, ny, v-1))
                  visited[x-1][ny] = True
              if x + 1 < R:
                if not wall[3][x][y] and not wall[c][x+1][y] and not visited[x+1][ny]:
                  q.append((x+1, ny, v-1))
                  visited[x+1][ny] = True

def tmp_controll(data):
  n_data = copy.deepcopy(data)
  for x in range(R):
    for y in range(C):
      for k in [0, 3]:
        nx = x + dx[k]
        ny = y + dy[k]
        if nx < R and ny < C and not wall[k][x][y]:
          p = abs(data[x][y] - data[nx][ny]) // 4
          if data[x][y] > data[nx][ny]:
            n_data[x][y] -= p
            n_data[nx][ny] += p
          else:
            n_data[x][y] += p
            n_data[nx][ny] -= p
  return n_data

def check_outside():
  for i in range(C):
    if data[0][i]:
      data[0][i] -= 1
    if data[R-1][i]:
      data[R-1][i] -= 1
  for i in range(1, R-1):
    if data[i][0]:
      data[i][0] -= 1
    if data[i][C-1]:
      data[i][C-1] -= 1

R, C, K = map(int,input().split())
data = []
s_area = [] # 온풍기 위치
c_area = [] # 온도 확인 장소
for i in range(R):
  data.append(list(map(int,input().split())))
  for j in range(C):
    if data[i][j]:
      if data[i][j] == 5:
        c_area.append((i, j))
      else:
        s_area.append((i, j, data[i][j]))
      data[i][j] = 0

# 벽 정보 입력
wall = [[[False] * C for _ in range(R)] for _ in range(4)]
for _ in range(int(input())):
  x, y, t = map(int,input().split())
  x-=1
  y-=1
  if t == 0: # 상, 하 위치 벽 설정
    wall[2][x][y] = True
    wall[3][x-1][y] = True
  else: # 좌, 우 위치 벽 설정
    wall[0][x][y] = True
    wall[1][x][y+1] = True

res = 0
while True:
  # 1. 온풍기 시작
  for x, y, c in s_area:
    start_controll(x, y, c-1)
  # 2. 온도 조절
  data = tmp_controll(data)
  # 3. 바깥 지역 온도 조절
  check_outside()
  # 4. 초콜릿 먹기
  res += 1
  # 5. 지정 지역 K 이하 인지 확인
  flag = True
  for x, y in c_area:
    if data[x][y] < K:
      flag = False
      break
  # 종료 조건 만족 시 종료
  if flag or res > 100:
    break
# 정답 출력
print(res)