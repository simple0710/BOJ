from collections import deque

def bfs(start, visited):
  cnt = 0
  # 방문하지 않은 지역인 경우 cnt = 1
  if not visited[start]:
    q = deque([start])
    visited[start] = True
    cnt = 1
    while q:
      v = q.popleft()
      for i in graph[v]:
        if not visited[i]:
          visited[i] = True
          q.append(i)

  return cnt

n, m = map(int,input().split())

# 데이터 입력 받기
graph = [list([]) for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
  a, b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

cnt = 0
for i in range(1, n+1):
  if bfs(i, visited) == 1:
    cnt += 1

print(cnt)