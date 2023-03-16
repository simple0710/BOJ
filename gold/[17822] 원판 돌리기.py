# 2023/03/14 Implementation
# https://www.acmicpc.net/problem/17822
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def near(x, y, value):
  global flag, res, cnt
  for i in range(4):
    nx = x + dx[i]
    ny = (y + dy[i]) % M
    if ny < 0:
      ny = M - 1
    if 0 <= nx < N:
      if value == board[nx][ny]:
        flag = True
        res -= value
        cnt -= 1
        board[nx][ny] = 0
        near(nx, ny, value)

N, M, T = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
cnt = N * M # 수의 개수
res = 0
for i in board:
  res += sum(i)

for _ in range(T):
  # x 배수의 원판을 d 방향으로 k 칸 회전
  x, d, k = map(int,input().split())
  for i in range(x-1, N, x): # 1. 원판 돌리기
    for _ in range(k):
      if d == 0:
        board[i].insert(0, board[i].pop())
      else:
        board[i].append(board[i].pop(0))

  flag = False
  for i in range(N): 
    for j in range(M):
      if board[i][j]: 
        # 2-1. 인접한 수가 있는 경우 인접한 수들을 지운다.
        near(i, j, board[i][j])
  if cnt == 0: # 수가 없으면 종료한다.
    break
  if not flag: # 2-2. 인접한 구역이 없는 경우
    aver = res / cnt
    for i in range(N):
      for j in range(M):
        if board[i][j]:
          # 평균 보다 높거나 낮은 경우 수의 값을 더하거나 뺀다.
          if aver > board[i][j]:
            res += 1
            board[i][j] += 1
          elif aver < board[i][j]:
            res -= 1
            board[i][j] -= 1
            if board[i][j] == 0: # 0이 되면 지워진다.
              cnt -= 1

# 정답 출력
print(res)