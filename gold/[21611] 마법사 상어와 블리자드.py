# 2023/09/15 Implementation, Simulation
# https://www.acmicpc.net/problem/21611
import sys
input = sys.stdin.readline

def ice_throw(d, distance): # 얼음 파편 던지기
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  x, y = N//2, N//2
  while 0 <= x + dx[d] < N and 0 <= y + dy[d] < N and distance:
    x += dx[d]
    y += dy[d]
    board[x][y] = 0
    distance -= 1

def fill_board(x, y, new_arr): # new_arr를 기반으로 보드 채우기
  dx = [0, 1, 0, -1]
  dy = [-1, 0, 1, 0]
  new_board = [[0] * N for _ in range(N)]
  fill_cnt = 0
  cnt = 0
  while cnt < N:
    for d in range(4):
      if d % 2 == 0:
        cnt += 1
      for _ in range(cnt):
        x += dx[d]
        y += dy[d]
        # 넘어가는 부분은 제외한다.
        if 0 <= x < N and 0 <= y < N and fill_cnt < min(len(new_arr), N * N):
          new_board[x][y] = new_arr[fill_cnt]
          fill_cnt += 1
      if cnt == N:
        break
  return new_board # 새 보드 반환


def same_number_check(four_check): # 연속된 숫자 확인
  check = four_check[0]
  cnt = 1
  new_arr = []
  for i in range(1, len(four_check)):
    if four_check[i] == check: # 같은 숫자 개수 증가
      cnt += 1
    else: # 같지 않은 경우
      if cnt < 4: # 연속된 수의 개수가 4미만인 경우
        new_arr += [check] * cnt # 배열에 추가
      else: # 연속딘 수의 개수가 4이상인 경우
        res[check] += cnt # 폭발한다.
      check = four_check[i]
      cnt = 1
  else:
    # 연속된 수의 개수 확인 후 폭발
    if cnt < 4:
      new_arr += [check] * cnt
    else:
      res[check] += cnt
  return new_arr # 새로운 배열 확인

def empty_place_fill(x, y):
  dx = [0, 1, 0, -1]
  dy = [-1, 0, 1, 0]
  cnt = 0
  four_check = []
  nx, ny = x, y
  while cnt < N:
    for d in range(4):
      if d % 2 == 0:
        cnt += 1
      for _ in range(cnt):
        nx += dx[d]
        ny += dy[d]
        # 빈 공간을 제외한 연속한 부분을 배열로 구성한다.
        if 0 <= nx < N and 0 <= ny < N and board[nx][ny]:
          four_check.append(board[nx][ny])
      if cnt == N:
        break
  new_arr = []
  if four_check: # 숫자가 있는 경우 같은 숫자를 찾는다.
    new_arr = same_number_check(four_check)

  # 폭발 여부 확인으로 반복을 결정한다.
  flag = True if len(new_arr) == len(four_check) else False
  return fill_board(x, y, new_arr), flag # 새 보드와 반복 여부 플래그 반환
  

def group_cnt_fill(x, y): # 숫자의 개수 확인
  dx = [0, 1, 0, -1]
  dy = [-1, 0, 1, 0]
  cnt = 0
  nx, ny = x, y
  new_group_arr = []
  check = 0
  group_cnt = 0
  while cnt < N:
    for d in range(4):
      if d % 2 == 0:
        cnt += 1
      for _ in range(cnt):
        nx += dx[d]
        ny += dy[d]
        # 빈 공간을 제외한 모든 공간을 확인한 후, 하나의 배열로 구성한다.
        if 0 <= nx < N and 0 <= ny < N and board[nx][ny] != 0:
          if check == board[nx][ny]:
            group_cnt += 1
          else:
            if check != 0:
              new_group_arr.extend([group_cnt, check])
            check = board[nx][ny]
            group_cnt = 1
      if cnt == N:
        break
  # 마지막 숫자 추가
  new_group_arr.extend([group_cnt, check])

  return fill_board(x, y, new_group_arr) # 새 배열 반환

def solution():
  global board, res
  res = [0, 0, 0, 0]
  x, y = N // 2, N // 2
  for direction, distance in magic:
    # 1. 블리자드 시전
    ice_throw(direction-1, distance)

    # 2. 4개 이상 연속하는 숫자 폭발 및 이동
    flag = False
    while not flag:
      board, flag = empty_place_fill(x, y)

    # 3. 구슬 그룹 변화(구슬의 수, 구슬의 숫자)
    board = group_cnt_fill(x, y)

  # i * 폭발한 i번의 구슬 개수를 반환한다.
  res = sum([res[i] * i for i in range(1, 4)])
  return res

def main():
  global N, board, magic
  N, M = map(int,input().split())
  board = [list(map(int,input().split())) for _ in range(N)]
  magic = [list(map(int,input().split())) for _ in range(M)]
  print(solution()) # 정답 출력

if __name__ == "__main__":
  main()