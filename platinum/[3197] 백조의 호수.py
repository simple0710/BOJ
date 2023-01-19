# 2023/01/18 BFS
# https://www.acmicpc.net/problem/3197
from collections import deque
import sys
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 백조 움직이기
def swan():
  while sq1:
    x, y = sq1.popleft()
    # 다른 백조와 만난 경우 True 반환
    if (x, y) == e:
      return True
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < R and 0 <= ny < C and not swan_visited[nx][ny]:
        if data[nx][ny] == '.': # 물인 경우 sq1에 저장
          sq1.append((nx, ny))
        else: # 물이 아닌 경우 sq2에 저장
          sq2.append((nx, ny))
        swan_visited[nx][ny] = True
  return False

def water():
  while wq1:
    x, y = wq1.popleft()
    data[x][y] = '.'
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < R and 0 <= ny < C and not water_visited[nx][ny]:
        if  data[nx][ny] == '.':
          wq1.append((nx, ny))
        else:
          wq2.append((nx, ny))
        water_visited[nx][ny] = True

R, C = map(int,input().split())
# 백조 위치, 다음 백조 위치, 물 위치, 다음 물이 될 위치
sq1, sq2, wq1, wq2 = deque(), deque(), deque(), deque() 
water_visited = [[False] * C for _ in range(R)]
swan_visited = [[False] * C for _ in range(R)]
data = []
for i in range(R):
  data.append(list(input().rstrip()))
  for j in range(C):
    # 백조의 위치 저장
    if data[i][j] == 'L':
      data[i][j] = '.'
      if not sq1:
        sq1.append((i, j))
        swan_visited[i][j] == True
      else:
        e = (i, j)
    # 물 위치 저장
    if data[i][j] == '.':
      wq1.append((i, j))
      water_visited[i][j] = True

t = 0
while True:
  water() # 물에서 이동을 해본다.
  if swan(): # 백조를 이동해 보고 True를 반환한 경우 반복문을 종료한다.
    break
  wq1 = wq2 # 임시 wq2를 wq1에 저장
  sq1 = sq2 # 임시 sq2를 sq1에 저장
  # 임시 큐를 비운다.
  wq2 = deque()
  sq2 = deque()
  t += 1 # 시간 증가

# 정답 출력
print(t)