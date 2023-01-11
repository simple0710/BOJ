# 2023/01/11 백트래킹
# https://www.acmicpc.net/problem/14620
import sys
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 꽃 총합 계산
def check(flower):
  p = 0
  visited = [[False] * N for _ in range(N)]
  for x, y in flower:
    p += data[x][y]
    visited[x][y] = True
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
        visited[nx][ny] = True
        p += data[nx][ny]
      else:
        return -1
  return p

# 꽃 위치 선택
def back(s, stx, sty):
  global res
  if len(s) == 3:
    c = check(s)
    if c != -1:
      res = min(res, c)
    return
  for i in range(stx, N):
    for j in range(0 if i != stx else sty, N):
      s.append((i, j))
      back(s, i, j)
      s.pop()

N = int(input())
data = [list(map(int,input().split())) for _ in range(N)]
res = int(sys.maxsize)
# 조사
back([], 0, 0)
# 정답 출력
print(res)