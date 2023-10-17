# 2023/09/05 BFS
# https://www.acmicpc.net/problem/26009
from collections import deque
import sys
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def traffic_point(a, b, visited): # 구역 체크
  if 0 <= a < N and 0 <= b < M:
    visited[a][b] = True

def traffic_check():
  visited = [[False] * M for _ in range(N)]
  for r, c, d in traffic: # 교통 정체 확인
    r-=1
    c-=1
    for i in range(d+1): # 경계선만 확인한다
      traffic_point(r-d+i, c-i, visited) # 위쪽 -> 왼쪽
      traffic_point(r-d+i, c+i, visited) # 위쪽 -> 오른쪽
      traffic_point(r+i, c-d+i, visited) # 왼쪽 -> 아래쪽
      traffic_point(r+d-i, c+i, visited) # 아래쪽 -> 오른쪽
  return visited

def solution():
  traffic_visited = traffic_check()
  q = deque([(0, 0)])
  visited = [[-1] * M for _ in range(N)]
  visited[0][0] = 0
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == -1 and not traffic_visited[nx][ny]:
        q.append((nx, ny))
        visited[nx][ny] = visited[x][y] + 1
  # 목적지에 도착한 경우 YES와 최소 이동 횟수 반환
  # 목적지에 도착하지 못한 경우 NO반환
  return f'YES\n{visited[N-1][M-1]}' if visited[N-1][M-1] != -1 else 'NO'

if __name__ == "__main__":
  N, M = map(int,input().split())
  K = int(input())
  traffic = [list(map(int,input().split())) for _ in range(K)]
  print(solution()) # 정답 출력