# 2023/08/21 Implementation, BFS
# https://www.acmicpc.net/problem/16569
from collections import deque, defaultdict
import sys
input = sys.stdin.readline

def solution(N, M, X, Y, map_, fire, visited):
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  q = deque([(X, Y)])
  visited[X][Y] = True
  res1, res2 = map_[X][Y], 0
  time = 0
  while q:
    for x, y in fire[time]: # 해당 시간에 움직이는 화산 폭발
      if visited[x][y] != 'F': # 폭파할 자리가 아닌 경우
        visited[x][y] = 'F'
        for i in range(4):
          nx = x + dx[i]
          ny = y + dy[i]
          if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] != 'F':
            fire[time+1].add((nx, ny))

    if time > 0:
      for _ in range(len(q)): # 재상이가 움직이는 순서
        x, y = q.popleft()
        for i in range(4):
          nx = x + dx[i]
          ny = y + dy[i]
          if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == -1:
            visited[nx][ny] = True
            q.append((nx, ny))
            if map_[nx][ny] > res1: # 가장 높은 곳인 경우 값 갱신
              res1 = map_[nx][ny]
              res2 = time
    time += 1
  # 가장 높은 고도, 해당 고도까지 걸리는 최소 시간 반환
  return res1, res2

def main():
  N, M, V = map(int,input().split())
  X, Y = map(int,input().split())
  map_ = [list(map(int,input().split())) for _ in range(N)]
  fire = defaultdict(set)
  visited = [[-1] * M for _ in range(N)]
  for _ in range(V):
    x, y, t = map(int,input().split())
    fire[t].add((x-1, y-1))
    visited[x-1][y-1] = 'f' # 터지기 전의 화산 위치 표시
  h, d = solution(N, M, X-1, Y-1, map_, fire, visited) # 탐색 시작
  # 가장 높은 고도, 해당 고도까지 걸리는 최소 시간 반환
  print(h, d) # 정답 출력
    
if __name__ == "__main__":
  main()