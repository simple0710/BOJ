# 2023/12/24 Bruteforcing, Backtracking
# https://www.acmicpc.net/problem/16945
import sys
input = sys.stdin.readline

def res_check():
  # 한 줄의 합
  check_sum = magic_squre[0] + magic_squre[1] + magic_squre[2]
  for i in range(3):
    # 가로, 세로의 합과 기존에 구한 값을 비교한다.
    # 비교한 값이 같지 않다면 False를 return한다.
    col_v = sum(magic_squre[i*3:i*3+3])
    row_v = magic_squre[i] + magic_squre[i+3] + magic_squre[i+6]
    if check_sum != col_v or check_sum != row_v:
      return False
  # 각 대각선의 값과 기존에 구한 값을 비교한다.
  # 비교한 값이 같지 않다면 False를 return한다.
  left_to_right = magic_squre[0] + magic_squre[4] + magic_squre[8]
  right_to_left = magic_squre[2] + magic_squre[4] + magic_squre[6]
  if check_sum != left_to_right or check_sum != right_to_left:
    return False
  return True

def back(depth):
  global res, magic_squre
  if depth == 9: # 모든 경우를 확인 완료
    if res_check(): # 매직 스퀘어가 될 수 있는지 확인한다.
      # 비용 계산 후, 정답을 최솟값으로 갱신한다.
      cost = 0
      for i in range(9): cost += abs(squre[i] - magic_squre[i])
      res = min(res, cost)
    return

  for i in range(1, 10):
    if number_check[i]: continue
    magic_squre[depth] = i # 현재 위치에 수 저장
    number_check[i] = True
    back(depth+1) # 다음 칸으로 넘어간다.
    number_check[i] = False

def main():
  global magic_squre, squre, res, number_check
  squre = []
  for _ in range(3):
    for i in list(map(int,input().split())):
      squre.append(i)
  res = int(1e9)
  magic_squre = [[] for _ in range(9)]
  number_check = [False] * 10
  back(0) # 탐색 시작
  print(res) # 비용의 최솟값을 출력한다.

if __name__ == "__main__":
  main()