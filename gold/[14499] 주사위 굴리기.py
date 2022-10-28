import sys
input = sys.stdin.readline

def solution(x, y):
  move_type = [(0, 1), (0, -1), (-1, 0), (1, 0)]
  for move in moves:
    nx = x + move_type[move-1][0]
    ny = y + move_type[move-1][1]
    if 0 <= nx < n and 0 <= ny < m:
      x, y = nx, ny
      turn(move)
      # 바닥이 0인 경우
      if board[nx][ny] == 0:
        board[nx][ny] = dice[-1]
      else:
        dice[-1] = board[nx][ny]
        board[nx][ny] = 0
      # 맨 위 출력
      print(dice[0])
# 해당 방향으로 회전할 경우의 주사위 상태를 변경한다
def turn(n):
  a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
  if n == 1: # 동
    dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c
  elif n == 2: # 서
    dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d
  elif n == 3: # 남
    dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b
  else: # 북
    dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e

# 정보 입력
n, m, x, y, k = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
moves = list(map(int,input().split()))
dice = [0, 0, 0, 0, 0, 0]
solution(x, y)