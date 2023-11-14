# 2023/07/13 BFS
# https://www.acmicpc.net/problem/24446
from collections import deque
import sys
input = sys.stdin.readline

def bfs(): # 너비 우선 탐색
  q = deque()
  q.append(R)
  visited = [-1] * (N+1)
  visited[R] = 0
  while q:
    v = q.popleft()
    for i in sorted(data[v]):
      if visited[i] == -1: # 방문하지 않은 경우
        visited[i] = visited[v] + 1
        q.append(i)
  for i in visited[1:]: # 정답 출력
    print(i)

N, M, R = map(int,input().split())
data = [[] for _ in range((N+1))]
for _ in range(M):
  u, v = map(int,input().split())
  data[u].append(v)
  data[v].append(u)
# 탐색 시작
bfs()