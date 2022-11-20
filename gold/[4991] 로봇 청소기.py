# 2022/11/18 BFS
from collections import deque
from itertools import permutations
import sys
input = sys.stdin.readline

# x, y부터의 거리를 구하는 함수
def bfs(x, y):
  visited = [[False] * W for _ in range(H)]
  visited[x][y] = 1
  q = deque()
  q.append((x, y))
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny] and data[nx][ny] != 'x':
        visited[nx][ny] = visited[x][y] + 1
        q.append((nx, ny))
  # 방문 기록 반환
  return visited
  
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
while True:
  W, H = map(int,input().split())
  # 종료 조건
  if W == 0 and H == 0:
    break

  # 그래프, 시작 지점, 더러운 칸의 위치 저장
  data = []
  dirst = []
  for i in range(H):
    data.append(list(input().rstrip()))
    for j in range(W):
      if data[i][j] == 'o':
        data[i][j] == '.'
        stx, sty = i, j
      if data[i][j] == '*':
        dirst.append((i, j))
  visited = bfs(stx, sty)

  flag = 0
  r_2 = [] # 시작 위치에서 먼지가 있는 곳의 거리를 저장하는 리스트
  for i, j in dirst:
    # 더러운 칸에 이동 기록이 없는 경우 flag = 1
    if not visited[i][j]:
      flag = 1
      break
    r_2.append(visited[i][j]-1)
  # flag = 1인 경우 -1 출력
  if flag:
    print(-1)
    continue
  # 더러운 칸 간의 이동거리를 2차원 배열에 저장
  dirst_2 = [[0] * len(dirst) for _ in range(len(dirst))]
  for i in range(len(dirst) - 1):
    # 해당 더러운 칸에서 움직인 거리 저장
    c = bfs(dirst[i][0], dirst[i][1])
    for j in range(i + 1, len(dirst)):
      dirst_2[i][j] = c[dirst[j][0]][dirst[j][1]] - 1
      dirst_2[j][i] = dirst_2[i][j]

  # 이전에 수행한 이동거리에 순열을 생성
  p = list(permutations([i for i in range(len(dirst_2))]))
  res = sys.maxsize
  for i in p:
    dist = 0
    dist += r_2[i[0]]
    nfrom = i[0]
    for j in range(1, len(i)):
      nto = i[j]
      dist += dirst_2[nfrom][nto]
      nfrom = nto
    # 그 합이 res 보다 작다면 res = dist
    res = min(res, dist)

  # 정답 출력
  print(res)
