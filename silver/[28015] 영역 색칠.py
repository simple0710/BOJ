# 2023/09/24 Greedy
# https://www.acmicpc.net/problem/28015
import sys
input = sys.stdin.readline

def color_check(check): # 색 확인
  cnt = 1
  for k in range(1, len(check)):
    if check[k] != check[0] and check[k] != check[k-1]:
      cnt += 1
  return cnt

def solution():
  res = 0
  for i in range(N):
    check = []
    for j in range(M):
      if board[i][j]: # 칠한 부분인 경우
        check.append(board[i][j])
      elif check: # 색을 마주했던 적이 있는 경우
        res += color_check(check)
        check.clear()
    if check: # 색을 마주했던 적이 있는 경우
      res += color_check(check)
  return res # 붓질 횟수 반환

def solution2():
  res = 0
  for line in board:
    start = 0
    his = 0
    for index in range(M):
      if line[index] == 0: # 칠하지 않은 곳인 경우
        if start != 0: # 색을 지나쳤었던 경우
          res += his//2 + 1
          start = 0
          his = 0
        elif start != line[index]: # 다른 색인 경우
          his += 1
          start = line[index] # 색 변경
    if his != 0: # 색을 지나쳤었던 경우
      res += his//2 + 1

def main():
  global N, M, board
  N, M = map(int,input().split())
  board = [list(map(int,input().split())) for _ in range(N)]
  print(solution()) # 코드 실행 및 정답 출력

if __name__ == "__main__":
  main()