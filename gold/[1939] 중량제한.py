# 2023/05/06 BFS, BinarySearch
# https://www.acmicpc.net/problem/1939
from collections import deque

def bfs(mid):
  q = deque()
  q.append(S)
  visited = [False] * (N + 1)
  visited[S] = True
  while q:
    v = q.popleft()
    if v == E: # 목적지에 도착한 경우
      return True
    for nx, nc in limit[v]:
      # 방문하지 않았고, 중량을 넘지 않은 경우
      if not visited[nx] and mid <= nc:
        q.append(nx)
        visited[nx] = True
  # 도착할 수 없는 경우
  return False

N, M = map(int,input().split())
limit = [[] for _ in range(N + 1)]
for _ in range(M):
  A, B, C = map(int,input().split())
  limit[A].append((B, C))
  limit[B].append((A, C))

S, E = map(int,input().split())
s, e = 0, int(1e9)
# 이진 탐색으로 가능한 중량 탐색
while s <= e:
  mid = (s + e) // 2
  if bfs(mid):
    s = mid + 1
  else:
    e = mid - 1
# 정답 출력
print(e)