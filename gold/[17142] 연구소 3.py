# 2022/12/03 BFS
# https://www.acmicpc.net/problem/17142
from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline

# 바이러스 조합으로 최소 시간을 구하는 함수
def virus_check(virus):
  time = -1
  for v in combinations(virus, M):
    check = bfs(v)
    if check == -1:
      continue
    # 시간이 지정되지 않았거나 check가 더 작은 경우 time을 변경
    if time == -1 or time > check:
      time = check
  # 걸리는 시간 반환
  return time

# 걸리는 시간을 구하는 함수
def bfs(v):
  visited = [[False] * N for _ in range(N)]
  # 시작 지점 방문 처리
  for x, y in v:
    visited[x][y] = True
  q = deque(v)
  time = 0
  check_cnt = len(virus)
  while q:
    p = 0
    # 한 사이클
    for _ in range(len(q)):
      x, y = q.popleft()
      # 아직 다 채워지지 않은 경우
      if check_cnt != total_cnt:
        p = 1
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] != 1:
          q.append((nx, ny))
          visited[nx][ny] = True
          # 빈 칸인 경우에만 cnt를 추가한다.
          if graph[nx][ny] != 2:
            check_cnt += 1
    time += p
  # 모든 칸을 채운 경우 time 반환
  if check_cnt == total_cnt:
    return time
  # 모든 칸을 채우지 못한 경우 -1 반환
  else:
    return -1

if __name__ == "__main__":
  N, M = map(int,input().split())
  graph = []
  virus = []
  total_cnt = 0
  for i in range(N):
    graph.append(list(map(int,input().split())))
    for j in range(N):
      if graph[i][j] != 1:
        total_cnt += 1 # 빈 칸의 수를 센다.
        if graph[i][j] == 2: # 바이러스 추가
          virus.append((i, j))

  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  # 처음부터 바이러스가 연구소를 다 채웠다면 0 출력
  if len(virus) == total_cnt:
    print(0)
  else:
    # 바이러스 탐색 후 시간 출력
    time = virus_check(virus)
    print(time)