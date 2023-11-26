# 2023/09/07 Implementation, Simulation, BFS
# https://www.acmicpc.net/problem/2933
from collections import deque
import sys
input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def shoot_find(x, y, d): # 막대기 던지기
  check = []
  while 0 <= y < C:
    if cave[x][y] == 'x': # 막대기와 미네랄이 만난 경우
      cave[x][y] = '.'
      for i in range(4): # 영향을 받는 클러스터 탐색
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C:
          if cave[nx][ny] == 'x': 
            check.append((nx, ny))
      break
    y += d
  return check # 남은 클러스터 반환

def cluster_group_find(x, y, color): # 클러스터 분류
  q = deque([(x, y)])
  visited[x][y] = color
  group = [(x, y)]
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and cave[nx][ny] == 'x':
        q.append((nx, ny))
        visited[nx][ny] = color
        group.append((nx, ny))
  return group # 그룹 반환

def solution():
  global cave, visited

  for turn in range(N):
    if turn % 2 == 0: # 왼쪽 -> 오른쪽
      y = 0
      d = 1
    else: # 오른쪽 -> 왼쪽
      y = C - 1
      d = -1
    # 1. 막대기 던지기
    nearby_area = shoot_find(R-shoot[turn], y, d) # 영향을 받은 클러스터 저장

    # 2. 클러스터 분류
    group = dict()
    group_down_cnt = dict()
    visited = [[False] * C for _ in range(R)]
    for idx, (x, y) in enumerate(nearby_area):
      if not visited[x][y]:
        # 클러스터 그룹 데이터 저장
        group[idx+1] = cluster_group_find(x, y, idx+1)
        group_down_cnt[idx+1] = 100

    # 3. 떨어지는 최소값 구하기
    for x in range(R-1, -1, -1):
      for y in range(C):
        if cave[x][y] == 'x' and visited[x][y]: # 영향을 받은 클러스터인 경우
          nx = x
          cave[x][y] = '.' # 미리 제거해 둔다.
          while nx + 1 < R: # 맨 위까지 확인한다.
            nx += 1
            # 영향을 받은 클러스터인 경우
            if cave[nx][y] == '.' and visited[nx][y]:
              # 같은 그룹에 속하지 않은 경우
              if visited[x][y] != visited[nx][y]:
                # 떨어지는 횟수 최소값 갱신
                down_cnt = nx - x - 1 + group_down_cnt[visited[nx][y]]
                group_down_cnt[visited[x][y]] = min(group_down_cnt[visited[x][y]], down_cnt)
              break
            # 영향을 받지 않는 미네랄인 경우 최소값 갱신
            elif cave[nx][y] == 'x':
              group_down_cnt[visited[x][y]] = min(group_down_cnt[visited[x][y]], nx - x - 1)
              break
          else: # 끝까지 도달한 경우 최소값 갱신
            group_down_cnt[visited[x][y]] = min(group_down_cnt[visited[x][y]], nx - x)

    # 4. 그룹에 맞게 x를 떨어뜨리기
    for now in group:
      for x, y in group[now]:
        cave[x+group_down_cnt[now]][y] = 'x'

if __name__ == "__main__":
  R, C = map(int,input().split())
  cave = [list(input().rstrip()) for _ in range(R)]
  N = int(input())
  shoot = list(map(int,input().split()))
  solution()
  # 정답 출력
  for i in cave:
    print(''.join(i))