# 시간 절약이라면 넓이 우선 탐색
from collections import deque
import sys
input = sys.stdin.readline

# 넓이 우선 탐색을 사용해야 한다.
def bfs(v, visited):
  cnt = 1
  queue = deque([v])
  visited[v] = True
  while queue:
    x = queue.popleft()
    for i in data[x]:
      if not visited[i]:
        visited[i] = True
        queue.append(i)
        cnt += 1
  return cnt

# 컴퓨터의 수와 신뢰하는 관계 입력
n, m = map(int, input().split())
data = [[] for _ in range(n+1)]

# 관계 생성
for _ in range(m):
  a, b = map(int, input().split())
  data[b].append(a) 

result = list() 
for i in range(1, n + 1):
  # bfs안에 추가해도 상관 없다.
  visited = [False] * (n+1)
  # cnt 값을 추가한다.
  result.append(bfs(i, visited))
max = max(result)

ans = list()
for i in range(n):
  # result[i]가 최대값이면 i+1 출력
  if max == result[i]:
    print(i+1, end = ' ')