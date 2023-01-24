# 2023/01/24 BFS
# https://www.acmicpc.net/problem/2636
from collections import deque
import sys
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
  sq = deque()
  while q:
    x, y = q.popleft()
    data[x][y] = 0
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N + 2 and 0 <= ny < M + 2 and not visited[nx][ny]:
        if data[nx][ny] == 1:
          sq.append((nx, ny))
        else:
          q.append((nx, ny))
        visited[nx][ny] = True
  return sq

# 치즈가 가장자리에 놓일 수 있는 경우
if __name__ == '__main__':
  N, M = map(int,input().split())
  cnt = 0
  data = [[0] * (M+2)]
  for i in range(N):
    data.append([0] + list(map(int,input().split())) + [0])
    for j in range(1, M+1):
      if data[i][j] == 1: # 치즈 개수 카운트
        cnt += 1
  data.append([0] * (M+2))

  q = deque()
  q.append((0, 0))
  visited = [[False] * (M + 2) for _ in range(N + 2)]
  visited[0][0] = True
  t = 0
  while True:
    q = bfs() # 임시큐를 q에 저장
    cnt -= len(q)
    if cnt == 0: # 치즈가 모두 녹기 전인 경우 정답 출력
      print(t+1) # 전부 녹는 시간
      print(len(q)) # 현재 남은 치즈 개수
      break
    t += 1