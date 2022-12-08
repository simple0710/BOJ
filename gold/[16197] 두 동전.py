# 2022/11/29 너비 우선탐색
# https://www.acmicpc.net/problem/16197
from collections import deque
import sys
input = sys.stdin.readline

def bfs():
  while coin:
    x1, y1, x2, y2, cnt = coin.popleft()

    # cnt가 10 이상인 경우 -1 반환
    if cnt >= 10:
      return -1

    for i in range(4):
      nx1 = x1 + dx[i]
      ny1 = y1 + dy[i]
      nx2 = x2 + dx[i]
      ny2 = y2 + dy[i]
      # 두 동전이 보드 위에 있는 경우
      if 0 <= nx1 < N and 0 <= ny1 < M and 0 <= nx2 < N and 0 <= ny2 < M:
        if board[nx1][ny1] == '#':
          nx1, ny1 = x1, y1
        if board[nx2][ny2] == '#':
          nx2, ny2 = x2, y2
        coin.append((nx1, ny1, nx2, ny2, cnt + 1))
      # 동전 2가 떨어진 경우
      elif 0 <= nx1 < N and 0 <= ny1 < M:
        return cnt + 1
      # 동전 1이 떨어진 경우
      elif 0 <= nx2 < N and 0 <= ny2 < M:
        return cnt + 1
      # 둘 다 빠진 경우
      else:
        continue
  return -1

# 정보 입력
N, M = map(int,input().split())

board = []
coin = deque()
cp = []
for i in range(N):
  board.append(list(map(str,input().rstrip())))
  for j in range(M):
    if board[i][j] == 'o':
      cp.append((i, j))
coin.append((cp[0][0], cp[0][1], cp[1][0], cp[1][1], 0))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 너비 우선 탐색 시작 및 정답 출력
print(bfs())