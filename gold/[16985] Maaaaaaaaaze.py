# 2023/11/21 Implementation, Bruteforcing, BFS
# https://www.acmicpc.net/problem/16985
from collections import deque
import sys
input = sys.stdin.readline
LENGTH = 5
MAX = 126
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

# 판 회전
def maze_turn(maze):
  return list(zip(*maze[::-1]))

# 경로 확인
def search_root():
  if res == 12: # 최소값인 경우 종료
    return MAX
  q = deque([(0, 0, 0)])
  visited = [[[-1] * LENGTH for _ in range(LENGTH)] for _ in range(LENGTH)]
  visited[0][0][0] = 0
  while q:
    z, x, y = q.popleft()
    # 목적지에 도착한 경우
    if (z, x, y) == (LENGTH-1, LENGTH-1, LENGTH-1):
      return visited[z][x][y]
    for i in range(6):
      nz = z + dz[i]
      nx = x + dx[i]
      ny = y + dy[i]
      # 범위 안인 경우
      if 0 <= nz < LENGTH and 0 <= nx < LENGTH and 0 <= ny < LENGTH:
        # 이동할 수 있는 지역인 경우
        if new_board[nz][nx][ny] == 1 and visited[nz][nx][ny] == -1:
          q.append((nz, nx, ny))
          visited[nz][nx][ny] = visited[z][x][y] + 1
  return MAX # 목적지에 도착하지 못한 경우

# 순열 리스트 추가
def pick_number_comb(s):
  if len(s) == 5: # 모든 수를 선택한 경우
    number_comb.append(s)
    return
  for i in range(5):
    if i not in s:
      pick_number_comb(s + [i])

def dfs(depth):
  global res
  if depth == 5:
    # 출구에 도착할 수 있는 경우
    if new_board[-1][-1][-1]:
      res = min(res, search_root())
    return
  for _ in range(4):
    # 입구에서 시작할 수 있는 경우
    if new_board[0][0][0]:
      dfs(depth+1)
    new_board[depth] = maze_turn(new_board[depth])

def solution():
  global res, new_board, number_comb
  res = MAX
  number_comb = []
  pick_number_comb([]) # 순열 확인
  # 순서를 정한 뒤, 회전 시작
  for comb in number_comb:
    new_board = [maze_board[i] for i in comb]
    dfs(0)
  # 최소 이동 횟수 반환
  return res if res != MAX else -1

def main():
  global maze_board
  maze_board = [[list(map(int,input().split())) for _ in range(LENGTH)] for _ in range(LENGTH)]
  print(solution()) # 최소 이동 횟수 출력

if __name__ == "__main__":
  main()