# 단순히 너비우선 탐색을 사용하면 끝이다.
from collections import deque

def bfs():
  q = deque()
  q.append(1)
  visited[1] = True
  cnt = 0
  while q:
    v = q.popleft()
    for i in data[v]:
      if not visited[i]:
        q.append(i)
        visited[i] = True
        cnt += 1
  return cnt

n = int(input())
data = [[] for _ in range(n + 1)]
visited = [False] * (n+1)

for _ in range(int(input())):
  x, y = map(int,input().split())
  data[x].append(y)
  data[y].append(x)

print(bfs())
