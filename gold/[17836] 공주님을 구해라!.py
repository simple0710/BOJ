# 2023/08/17 BFS
# https://www.acmicpc.net/problem/17836
from collections import deque
import sys
input = sys.stdin.readline
MAX = int(1e4) + 1

def solution(castle, N, M, T):
  dx = [1, 0, -1, 0]
  dy = [0, 1, 0, -1]
  q = deque([(0, 0)])
  visited = [[MAX] * M for _ in range(N)]
  visited[0][0] = 0
  s = MAX
  while q:
    x, y = q.popleft()
    if castle[x][y] == 2: # 그람을 구한 경우
      s = visited[x][y] + (N - 1 - x) + (M - 1 - y)
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == MAX:
        if castle[nx][ny] != 1: # 벽이 아닌 경우
          q.append((nx, ny))
          visited[nx][ny] = visited[x][y] + 1
  check = min(s, visited[N-1][M-1]) # 걸어간 경우와 그람을 구한 경우를 비교한다.
  if check <= T: # 제한 시간을 넘지 않은 경우 시간 반환
    return check
  else: # 제한 시간을 넘긴 경우
    return "Fail"

def main():
  N, M, T = map(int,input().split())
  castle = [list(map(int,input().split())) for _ in range(N)]
  res = solution(castle, N, M, T) # 코드 실행
  print(res) # 정답 출력

if __name__ == "__main__":
  main()