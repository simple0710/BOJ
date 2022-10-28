# 2022/10/27 너비우선탐색
from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int,input().split())
MAX = 10**5 + 1
visited = [0] * MAX
cnt = 0
def bfs(n):
  global cnt
  q = deque()
  q.append(n)
  while q:
    v = q.popleft()
    # 목적지에 도착한 경우
    if v == k:
      cnt += 1
      continue
    for nv in (v - 1, v + 1, v * 2):
      # 아직 방문하지 않았거나, 움직인 수의 차이가 나지 않는 경우
      if 0 <= nv < MAX and (not visited[nv] or visited[nv] == visited[v] + 1):
        visited[nv] = visited[v] + 1
        q.append(nv)
bfs(n)
print(visited[k])
print(cnt)