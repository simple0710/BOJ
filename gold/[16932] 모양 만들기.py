# 2023/12/25 BFS, DFS
# https://www.acmicpc.net/problem/16932
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# x, y위치부터 인접한 모든 지역에 그룹 값을 저장한다.
def check_cnt(x, y, group_color):
  q = deque([(x, y)])
  visited[x][y] = group_color
  cnt = 1
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and arr[nx][ny] == 1:
        visited[nx][ny] = group_color
        q.append((nx, ny))
        cnt += 1
  return cnt # 인접한 개수 반환

def find_res(x, y, group_cnt):
  group = set()
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < N and 0 <= ny < M:
      group.add(visited[nx][ny])
  # 현재 변경한 수와 각 그룹의 합을 더한다.
  v = 1 + sum([group_cnt.get(i, 0) for i in group])
  return v

def solution():
  global visited
  group_color = 1
  group_cnt = {}
  visited = [[0] * M for _ in range(N)]
  # 각 그룹에 해당하는 배열의 수의 개수를 구한다.
  for i in range(N):
    for j in range(M):
      if arr[i][j] == 1 and not visited[i][j]:
        # 인접한 개수를 딕셔너리에 그룹 이름으로 저장한다.
        group_cnt[group_color] = check_cnt(i, j, group_color)
        group_color += 1

  # 수(0) 하나를 변경했을 때, 만들 수 있는 모양의 최대 크기 탐색
  res = 1
  for i in range(N):
    for j in range(M):
      if arr[i][j] == 0:
        # 최댓값 갱신
        res = max(res, find_res(i, j, group_cnt))

  # 하나를 변경해서 만들 수 있는 모양의 최대 크기 반환
  return res

def main():
  global N, M, arr
  N, M = map(int,input().split())
  arr = [list(map(int,input().split())) for _ in range(N)]
  # 하나를 변경해서 만들 수 있는 모양의 최대 크기 출력
  print(solution())

if __name__ == "__main__":
  main()