# 2022/10/27 너비우선탐색
from collections import deque
import sys
input = sys.stdin.readline

# 너비우선 탐색
def bfs(s):
  q = deque()
  q.append(s)
  visited[s] = 1
  while q:
    v = q.popleft()
    for i in arr[v]:
      if not visited[i]:
        q.append(i)
        visited[i] = visited[v] + 1

# 깊이 우선 탐색
def dfs(v):
  # 함수 실행 전 visited[시작점] = 1로 정의해둔다.
  for i in arr[v]:
    if not visited[i]:
      visited[i] = visited[v] + 1
      dfs(i)

# 정보 입력
n = int(input())
arr = [[] for _ in range(n + 1)]
s, e = map(int,input().split())
m = int(input())
for _ in range(m):
  a, b = map(int,input().split())
  arr[a].append(b)
  arr[b].append(a)
visited = [False] * (n + 1)

# 깊이우선탐색
'''
visited[s] = 1 
dfs(s)
'''
# 너비우선탐색
bfs(s)

# 계산이 안되는 경우는 -1
if visited[e]:
  print(visited[e] - 1)
else:
  print(-1)