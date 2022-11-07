# 2022/11/06 위상정렬
from collections import deque
import sys
input = sys.stdin.readline

# 너비우선탐색/위상정렬
def topology_sort():
  s = list()
  q = deque()
  for i in range(1, N + 1):
    if in_degree[i] == 0:
      q.append(i)

  while q:
    now = q.popleft()
    s.append(now)
    for i in data[now]:
      in_degree[i] -= 1
      if in_degree[i] == 0:
        q.append(i)
  # 결과 출력
  for i in s:
    print(i, end = ' ')

# 정보 입력
N, M = map(int,input().split())
data = [[] for _ in range(N + 1)]
in_degree = [0] * (N + 1)

for _ in range(M):
  a, b = map(int,input().split())
  data[a].append(b)
  # 진입 차수 증가
  in_degree[b] += 1

topology_sort()