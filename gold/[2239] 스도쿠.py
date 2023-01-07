# 2022/12/16 백트래킹
import sys
input = sys.stdin.readline

def dfs(depth):
  # 끝까지 한 경우 출력
  if depth == len(zero):
    for i in board:
      print(''.join(map(str, i)))
    exit(0)

  x = zero[depth][0]
  y = zero[depth][1]
  for i in range(1, 10):
    if x_check(x, i) and y_check(y, i) and squre_check(x, y, i):
      board[x][y] = i
      dfs(depth+1)
      board[x][y] = 0

# 열 확인
def x_check(x, value):
  if value in board[x][0:]:
    return False
  else:
    return True

# 행 확인
def y_check(y, value):
  if value in [b[y] for b in board]:
    return False
  else:
    return True

# 사각형 칸 확인
def squre_check(x, y, value):
  start_x = x // 3 * 3
  start_y = y // 3 * 3
  for i in range(3):
    for j in range(3):
      if value == board[start_x + i][start_y + j]:
        return False
  return True

board = []
zero = []
for i in range(9):
  board.append(list(input().rstrip()))
  for j in range(9):
    # int형으로 변환
    board[i][j] = int(board[i][j])
    if board[i][j] == 0:
      zero.append((i, j))
      
# 백트래킹 시작
dfs(0)