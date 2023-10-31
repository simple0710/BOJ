# 2023/11/01 Implementation
# https://www.acmicpc.net/problem/7682
# O가 더 많은 경우
# 특정 말의 개수가 부족한 경우
# 게임이 끝났는데 말의 개수가 맞지 않은 경우
# X가 이기면 O보다 1개 많음, O가 이기면 같음
# 게임이 끝나지 않은 경우 ex) O..XX....
# 동시에 승리한 경우
import sys
input = sys.stdin.readline

# 열 확인
def check_row_win(board, v):
  start = 3 * (v//3)
  end = start + 3
  for i in range(start, end):
    if board[v] != board[i]: return 0
  return 1

# 행 확인
def check_col_win(board, v):
  start = v % 3
  end = 9
  for i in range(start, end, 3):
    if board[v] != board[i]: return 0
  return 1

# 대각선 확인
def check_diagonal_win(board, v):
  cnt = 0
  for i in range(0, 9, 4):
    if board[v] != board[i]: break
  else: cnt = 1
  for i in range(2, 7, 2):
    if board[v] != board[i]: break
  else: cnt = 1
  return cnt

def solution(board):
  # 해당 문자 : [개수, 3칸을 이은 횟수]
  cnt_dict = {
    'X' : [board.count('X'), 0],
    'O' : [board.count('O'), 0],
  }

  # 대각선 확인
  if board[4] != '.':
    cnt_dict[board[4]][1] = check_diagonal_win(board, 4)

  # 해당 위치에서 가로 방향 혹은 세로 방향으로 3칸을 이어져 있는지 확인
  for i in range(0, 9, 4):
    if board[i] != '.': # 빈 칸이 아닌 경우
      # 가로, 세로 확인
      cnt_dict[board[i]][1] += max(check_row_win(board, i), check_col_win(board, i))

  # X가 이긴 경우
  if 1 <= cnt_dict['X'][1] <= 2 and cnt_dict['O'][1] == 0:
    # 차이는 1이 될 수밖에 없다.
    if cnt_dict['X'][0] - cnt_dict['O'][0] == 1:
      return 'valid'
  # O가 이긴 경우
  elif cnt_dict['X'][1] == 0 and cnt_dict['O'][1] == 1:
    # 차이는 0이 될 수밖에 없다.
    if cnt_dict['X'][0] - cnt_dict['O'][0] == 0:
      return 'valid'
  # 누구도 이기지 못한 경우
  elif cnt_dict['X'][1] == 0 and cnt_dict['O'][1] == 0:
    # 모든 칸이 채워져야 한다.
    # 두 돌의 차이가 1이다.
    if cnt_dict['X'][0] == 5 and cnt_dict['O'][0] == 4:
      return 'valid'
  # 불가능
  return 'invalid'

def main():
  while True:
    data = input().rstrip()
    # end를 입력받는 경우 종료
    if data == 'end': break
    # 가능한 경우, 불가능한 경우 출력
    print(solution(data))

if __name__ == "__main__":
  main()