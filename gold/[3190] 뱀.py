# 2022/10/25
from collections import deque
import sys
input = sys.stdin.readline

# n : 보드의 크기
# k : 사과의 개수
n = int(input())
k = int(input())
graph = [[0] * n for _ in range(n)]
# 사과 위치 저장
for i in range(k):
  a, b = map(int,input().split())
  graph[a-1][b-1] = 2

# 특정 시간에 'L' or 'D' 저장
L = int(input())
dirDict = dict()
for i in range(L):
  x, c = input().rstrip().split()
  dirDict[int(x)] = c

# 정보 세팅
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
q = deque()
q.append((0, 0))
x, y = 0, 0
graph[x][y] = 1
time = 0
direction = 0

# 회전 연산
def turn(a):
  global direction
  if a == 'L':
    direction = (direction - 1) % 4
  else:
    direction = (direction + 1) % 4

while True:
  time += 1
  # 이동
  x += dx[direction]
  y += dy[direction]
  # 범위를 벗어났을 경우 종료
  if x < 0 or x >= n or y < 0 or y >= n:
    break
  # 사과인 경우
  if graph[x][y] == 2:
    graph[x][y] = 1
    q.append((x, y))
    if time in dirDict:
      turn(dirDict[time])
  # 꼬리 부분 지우고 머리로 옮기기
  elif graph[x][y] == 0:
    graph[x][y] = 1
    q.append((x, y))
    tx, ty = q.popleft()
    graph[tx][ty] = 0
    if time in dirDict:
      turn(dirDict[time])
  else:
    break

print(time)