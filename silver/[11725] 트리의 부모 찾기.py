# 2023/05/01 Tree, BFS
# https://www.acmicpc.net/problem/11725
from collections import defaultdict, deque
import sys
input = sys.stdin.readline

def bfs():
  q = deque()
  q.append(1)
  visited = [False] * (N + 1)
  while q:
    v = q.popleft()
    for i in data[v]: # 자식 노드 탐색
      if not visited[i]: # 방문하지 않은 경우
        q.append(i)
        visited[i] = v # 부모 노드 지정
  for i in visited[2:]: # 정답 출력
    print(i)

N = int(input())
data = defaultdict(list)
for _ in range(N - 1):
  a1, a2 = list(map(int,input().split()))
  data[a1].append(a2)
  data[a2].append(a1)
bfs() # 탐색 시작