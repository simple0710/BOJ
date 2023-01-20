# 2023/01/20 Backtracking, Bruteforce
# https://www.acmicpc.net/problem/9207
import sys, copy
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(depth, data, flag):
  global res, move
  if flag: # 움직일 수 있는 핀이 없는 경우
    if depth > move:
      move = depth
      res = total_pin - move
    return
  flag = True
  for x in range(h): # 전 지역 탐색
    for y in range(w):
      if data[x][y] == 'o': # 핀인 경우 4방향 탐색
        for i in range(4):
          nx = x + dx[i]
          ny = y + dy[i]
          fx = nx + dx[i]
          fy = ny + dy[i]
          if (0 <= nx < h and 0 <= ny < w) and (0 <= fx < h and 0 <= fy < w):
            if data[nx][ny] == 'o':
              if data[fx][fy] == '.': # 이동해보기
                flag = False
                data[x][y] = '.'
                data[fx][fy] = 'o'
                data[nx][ny] = '.'
                n_data = copy.deepcopy(data) # 함수에 data칸을 없애면 되는 듯 하다.
                dfs(depth+1, n_data, False)
                data[x][y] = 'o'
                data[fx][fy] = '.'
                data[nx][ny] = 'o'
  if flag: # 움직일 수 있는 핀이 없는 경우
    dfs(depth, data, True)

T = int(input())
h, w = 5, 9
while True:
  T -= 1
  total_pin = 0
  data = []
  for i in range(h):
    data.append(list(input().rstrip()))
    for j in range(w):
      if data[i][j] == 'o':
        total_pin += 1
  move = 0
  res = total_pin
  dfs(move, data, False) # 탐색 시작
  print(res, move) # 정답 출력
  if T == 0:
    break
  input()