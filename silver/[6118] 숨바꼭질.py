# 2023/05/09 BFS
# https://www.acmicpc.net/problem/6118
from collections import deque
import sys
input = sys.stdin.readline

def bfs():
  q = deque([1])
  visited = [False] * (N + 1)
  visited[1] = 1
  while q:
    v = q.popleft()
    for i in data[v]:
      if not visited[i]:
        q.append(i)
        visited[i] = visited[v] + 1
  check = max(visited) # 최댓값 저장
  # 정답(숨을 장소, 거리, 같은 거리 개수) 출력
  print(visited.index(check), check - 1, visited.count(check))

N, M = map(int,input().split())
data = [[] for _ in range(N + 1)]
for _ in range(M):
  a, b = map(int,input().split())
  data[b].append(a)
  data[a].append(b)
# 탐색 시작
bfs()