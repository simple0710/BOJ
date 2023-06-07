# 2023/06/07 BFS
# https://www.acmicpc.net/problem/24445
from collections import deque
import sys
input = sys.stdin.readline

def bfs():
  q = deque()
  q.append(R)
  visited = [0] * (N + 1)
  visited[R] = 1
  cnt = 2
  while q:
    v = q.popleft()
    for i in sorted(data[v], reverse=True): # 내림차 순 정렬
      if not visited[i]:
        visited[i] = cnt
        cnt += 1
        q.append(i)
  # 정답 출력
  for i in visited[1:]:
    print(i)

N, M, R = map(int,input().split())
data = [[] for _ in range(N + 1)]
for _ in range(M):
  a, b =  map(int, input().split())
  data[a].append(b)
  data[b].append(a)
bfs()