# 2023/12/27 BFS, DFS
# https://www.acmicpc.net/problem/16174
from collections import deque

def solution():
  dx = [0, 1]
  dy = [1, 0]
  x, y = 0, 0
  q = deque([(x, y)])
  visited = [[False] * N for _ in range(N)]
  while q:
    x, y = q.popleft()
    for i in range(2):
      # 현재 밟고 있는 발판의 수만큼 이동한다.
      nx = x + dx[i] * board[x][y]
      ny = y + dy[i] * board[x][y]
      if nx < N and ny < N and not visited[nx][ny]:
        q.append((nx, ny))
        visited[nx][ny] = True
  # 목적지 도달 여부 반환
  if visited[-1][-1]: return 'HaruHaru'
  return 'Hing'

def main():
  global N, board
  N = int(input())
  board = [list(map(int,input().split())) for _ in range(N)]
  print(solution()) # 목적지 도달 여부 출력

if __name__ == "__main__":
  main()