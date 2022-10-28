# 2022/10/28 너비우선탐색
from collections import deque
import sys
input = sys.stdin.readline

def bfs(v):
  q = deque()
  q.append(v)
  while q:
    v = q.popleft()
    visited[v] = True
    for x in data[v]:
      if not visited[x]:
        q.append(x)

for _ in range(int(input())):
  n = int(input())
  arr = list(map(int,input().split()))

  # 데이터 생성
  data = [[] for _ in range(n + 1)]
  for i in range(1, n + 1):
    data[i].append(arr[i-1])
    data[arr[i-1]].append(i)

  visited = [False] * (n + 1)
  cnt = 0
  for i in range(1, n+1):
    if not visited[i]:
      cnt += 1
      bfs(i)
      
  # 출력
  print(cnt)