import sys
# 10**6을 하니까 메모리 초과가 나온다...
sys.setrecursionlimit(10000)

# 깊이 우선 탐색
def dfs(v):
  visited[v] = True
  for i in graph[v]:
    if not visited[i]:
      dfs(i)

n, m = map(int,input().split())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

# 데이터 입력
for _ in range(m):
  a, b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

cnt = 0
# 방문하지 않은 곳 방문
for j in range(1, n + 1):
  if not visited[j]:
    dfs(j)
    cnt += 1

print(cnt)