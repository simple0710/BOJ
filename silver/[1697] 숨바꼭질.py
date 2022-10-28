# 2022/10/27 너비우선탐색
from collections import deque
import sys
input = sys.stdin.readline

def bfs(v):
  q = deque()
  q.append(v)
  while q:
    v = q.popleft()
    # 목적지에 도달했을 경우 출력
    if v == k:
      print(visited[v])
      break
    # 움직임
    for nv in (v - 1, v + 1, v * 2):
      if 0 <= nv < len(visited) and not visited[nv]:
        q.append(nv)
        visited[nv] = visited[v] + 1
  
n, k = map(int,input().split())
MAX = 10**5
visited = [0] * (MAX + 1)
bfs(n)