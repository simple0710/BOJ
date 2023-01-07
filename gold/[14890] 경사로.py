# 2023/01/03 구현
# https://www.acmicpc.net/problem/14890
import sys
input = sys.stdin.readline

def solution(data):
  global res
  # 왼쪽에서 오른쪽으로 이동
  visited_1 = [[False] * N for _ in range(N)]
  for i in range(N):
    visited_1[i][0] = True
    s_left = data[i][0]
    s_cnt = 1
    for j in range(1, N):
      if data[i][j] == s_left:
        visited_1[i][j] = True
        s_cnt += 1
      elif abs(data[i][j] - s_left) == 1:
        if data[i][j] > s_left:
          if s_cnt >= L:
            visited_1[i][j] = True
            s_cnt = 1
          else:
            break
        else:
          visited_1[i][j] = True
          s_cnt = 1-L
        s_left = data[i][j]
      else:
        break
  # 오른쪽에서 왼쪽으로 이동
  visited_2 = [[False] * N for _ in range(N)]
  for i in  range(N):
    visited_2[i][-1] = True
    s_right = data[i][-1]
    s_cnt = 1
    for j in range(N-2, -1, -1):
      if data[i][j] == s_right:
        visited_2[i][j] = True
        s_cnt += 1
      elif abs(data[i][j] - s_right) == 1:
        if data[i][j] > s_right:
          if s_cnt >= L:
            visited_2[i][j] = True
            s_cnt = 1
          else:
            break
        else:
          visited_2[i][j] = True
          s_cnt = 1-L
        s_right = data[i][j]
      else:
        break

  for i in range(N):
    flag = True
    for j in range(N):
      if not visited_1[i][j] or not visited_2[i][j]:
        flag = False
        break
    if flag:
      res += 1

N, L = map(int,input().split())
data_row = [list(map(int,input().split())) for _ in range(N)]
data_col = list(zip(*data_row))
res = 0
solution(data_row)
solution(data_col)
print(res)