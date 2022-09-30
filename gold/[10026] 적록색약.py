from collections import deque
import sys
import copy
input = sys.stdin.readline

def bfs(x, y, word, graph):
  q = deque()
  q.append((x, y))
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == word:
        graph[nx][ny] = 0
        q.append((nx, ny))

n = int(input())
data = [list(map(str, input().rstrip())) for _ in range(n)]

RGB = copy.deepcopy(data)
RB = copy.deepcopy(data)
RGB_area = 0
RB_area = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
  for j in range(n):
    if RB[i][j] == "R":
      RB[i][j] = "G"

for i in range(n):
  for j in range(n):
    if RGB[i][j] != 0:
      bfs(i, j, RGB[i][j], RGB)
      RGB[i][j] = 0
      RGB_area += 1
    if RB[i][j] != 0:
      bfs(i, j, RB[i][j], RB)
      RB[i][j] = 0
      RB_area += 1

print(RGB_area, RB_area)