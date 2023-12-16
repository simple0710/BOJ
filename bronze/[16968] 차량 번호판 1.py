# 2023/12/16 Math, Combinatorics
# https://www.acmicpc.net/problem/16968
def main():
  board = input()
  board_type = {'c': 26, 'd': 10}
  res = board_type[board[0]]
  for i in range(1, len(board)):
    now = board_type[board[i]]
    # 연속되는 경우 -1을 한다.
    if board[i-1] == board[i]: now -= 1
    res *= now # 번호판 개수 계산
  print(res) # 가능한 차량 번호판의 개수 출력

if __name__ == "__main__":
  main()