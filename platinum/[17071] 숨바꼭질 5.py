# 2023/01/04 BFS
# https://www.acmicpc.net/problem/17071
from collections import deque
import sys
input = sys.stdin.readline
MAX = 500000

def bfs():
  q = deque()
  q.append((N, 0))
  visited[0][N] = 0
  while q:
    v, t = q.popleft()
    flag = t % 2 # 홀수, 짝수 판단
    for nv in (v+1, v-1, v*2):
      # 1-flag 는 이전 시간에서 다음 시간으로 가는 값
      if 0 <= nv <= MAX and visited[1-flag][nv] == -1:
        visited[1-flag][nv] = t + 1
        q.append((nv, t+1))

N, K = map(int,input().split())
# visited[n][0] : 짝수 시간에 위치 n을 방문한 최소시간
# visited[n][1] : 홀수 시간에 위치 n을 방문한 최소시간
visited = [[-1 for _ in range(MAX+1)] for _ in range(2)]

bfs()

# 방문할 수 있는지 확인해본다.
t = 0
flag = 0
res = -1
while K <= 500000:
  if visited[flag][K] != -1:
    if visited[flag][K] <= t:
      res = t
      break
  flag = 1-flag
  t += 1
  K += t

# 정답 출력
print(res)