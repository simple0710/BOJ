# 2022/12/14 백트래킹
# https://www.acmicpc.net/problem/12100
import sys, copy
input = sys.stdin.readline

# 보드, 방향, 횟수
def dfs(board, turn, depth):
  global res
  # 깊이가 5인 경우 판 전체 확인
  if depth == 5:
    for col in board:
      res = max(res, max(col))
    return
  n_board = copy.deepcopy(board)
  if turn == 0: # 왼쪽으로 진행
    for i in range(N):
      for j in range(N):
        if n_board[i][j] == 0:
          continue
        move_left(n_board, i, j)
  elif turn == 1: # 오른쪽으로 진행
    for i in range(N):
      for j in range(N-1, -1, -1):
        if n_board[i][j] == 0:
          continue
        move_right(n_board, i, j)
  elif turn == 2: # 위쪽으로 진행
    for i in range(N):
      for j in range(N):
        if n_board[j][i] == 0:
          continue
        move_up(n_board, j, i)
  else: # 아래로 진행
    for i in range(N):
      for j in range(N-1, -1, -1):
        if n_board[j][i] == 0:
          continue
        move_down(n_board, j, i)
  # 각 방향으로 다시 진행
  for i in range(4):
    dfs(n_board, i, depth + 1)

# 이동하려는 반대편에서 같은 수를 찾는다.
# 이동한다.
def move_right(board, x, y):
  for i in range(y-1, -1, -1):
    if board[x][i] != 0:
      if board[x][y] == board[x][i]:
        board[x][y] = board[x][y] * 2
        board[x][i] = 0
        break
      else:
        break
  value = board[x][y]
  board[x][y] = 0
  for i in range(y+1, N):
    if board[x][i] == 0:
      y = i
    else:
      break
  board[x][y] = value

def move_left(board, x, y):
  for i in range(y+1, N):
    if board[x][i] != 0:
      if board[x][y] == board[x][i]:
        board[x][y] = board[x][y] * 2
        board[x][i] = 0
        break
      else:
        break
  value = board[x][y]
  board[x][y] = 0
  for i in range(y-1, -1, -1):
    if board[x][i] == 0:
      y = i
    else:
      break
  board[x][y] = value

def move_down(board, x, y):
  for i in range(x-1, -1, -1):
    if board[i][y] != 0:
      if board[x][y] == board[i][y]:
        board[x][y] = board[x][y] * 2
        board[i][y] = 0
        break
      else:
        break
  value = board[x][y]
  board[x][y] = 0
  for i in range(x+1, N):
    if board[i][y] == 0:
      x = i
    else:
      break
  board[x][y] = value

def move_up(board, x, y):
  for i in range(x+1, N):
    if board[i][y] != 0:
      if board[x][y] == board[i][y]:
        board[x][y] = board[x][y] * 2
        board[i][y] = 0
        break
      else:
        break
  value = board[x][y]
  board[x][y] = 0
  for i in range(x-1, -1, -1):
    if board[i][y] == 0:
      x = i
    else:
      break
  board[x][y] = value

if __name__ == "__main__":
  N = int(input())
  board = [list(map(int,input().split())) for _ in range(N)]

  res = 0
  # 탐색 시작
  for i in range(4):
    dfs(board, i, 0)
  
  # 정답 출력
  print(res)