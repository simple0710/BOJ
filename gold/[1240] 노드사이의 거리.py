# 2023/07/28 BFS, Trees
# https://www.acmicpc.net/problem/1240
from collections import deque
import sys
MAX = sys.maxsize

def bfs(a, b):
  q = deque([a])
  visited = [MAX] * (N + 1)
  visited[a] = 0
  while q:
    now = q.popleft()
    for next, distance in node[now]:
      if visited[next] == MAX:
        q.append(next)
        visited[next] = min(visited[next], visited[now] + distance)
  # 최단 거리 반환
  return visited[b]

N, M = map(int,input().split())
node = [[] for _ in range(N+1)]
for _ in range(N-1): # 노드 간의 거리 데이터 저장
  a, b, d = map(int,input().split())
  node[a].append((b, d))
  node[b].append((a, d))

for _ in range(M): # 시작점과 도착점 입력
  a, b = map(int,input().split())
  # 탐색 후 정답 출력
  print(bfs(a, b))