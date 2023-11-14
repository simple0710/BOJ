# 2023/07/04 BFS, Sorting
# https://www.acmicpc.net/problem/24444
from collections import deque
import sys
input = sys.stdin.readline

def bfs(s):
  q = deque()
  q.append(s)
  visited = [0] * (N + 1)
  visited[s] = 1
  cnt = 2
  while q:
    v = q.popleft()
    for i in graph[v]:
      if not visited[i]: # 방문하지 않은 지역 확인
        visited[i] = cnt
        cnt += 1
        q.append(i)
  # 정답 출력
  for i in visited[1:]:
    print(i)

N, M, R = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
  a, b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)
for i in graph: # 그래프 정렬
  i.sort()
# 탐색 시작
bfs(R)