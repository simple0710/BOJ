# 2023/07/09 BFS
# https://www.acmicpc.net/problem/16173
# 외곽으론 나가지 못한다.
# 출발 : 가장 왼쪽, 가장 위의 칸
# 이동 : 오른쪽, 아래
# 도착 : 가장 오른쪽, 가장 아래 칸
# 이동 가능한 칸 : 현재 밟고 있는 칸의 수와 동일하게 이동
from collections import deque

def bfs():
  q = deque()
  q.append((0, 0))
  visited = [[False] * N for _ in range(N)]
  visited[0][0] = True
  while q:
    x, y = q.popleft()
    now = area[x][y] # 현재 발판
    if now == -1: # 목적지에 도착한 경우
      return "HaruHaru"
    for nx, ny in [(x, y + now), (x + now, y)]: # 점프는 한 방향으로만 가능
      if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
        visited[nx][ny] = True
        q.append((nx, ny))
  return "Hing" # 도달할 수 없는 경우
  
N = int(input())
area = [list(map(int,input().split())) for _ in range(N)]
# 탐색 및 정답 출력
print(bfs())