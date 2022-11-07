# 2022/11/07 너비우선탐색, 위상정렬
from collections import deque
import sys
input = sys.stdin.readline

def topology_sort():
  s = []
  q = deque()
  # 진입 차수가 0인 경우 추가
  for i in range(1, N+1):
    if in_degree[i] == 0:
      q.append(i)

  while q:
    now = q.popleft()
    s.append(now)
    for i in graph[now]:
      in_degree[i] -= 1
      # 진입 차수가 0인 경우 추가
      if in_degree[i] == 0:
        q.append(i)
  # 모든 순서가 정해지지 않은 경우 0 출력
  if len(s) < N:
    print(0)
    return
  # 결과 출력
  for i in s:
    print(i)

# 정보 입력
N, M = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(M)]
in_degree = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
for i in data:
  for j in range(2, len(i)):
    graph[i[j-1]].append(i[j]) 
    in_degree[i[j]] += 1

topology_sort()