# 2023/07/22 BFS
# https://www.acmicpc.net/problem/12761
from collections import deque

def bfs():
  q = deque([(N)])
  visited = [-1] * 100001
  visited[N] = 0
  while q:
    v = q.popleft()
    # 움직이는 타입
    for m in [v-1, v+1, v-A, v+A, v-B, v+B, v*A, v*B]:
      if 0 <= m <= 100000 and visited[m] == -1: # 범위 내 이동할 수 있는 공간 탐색
        q.append(m)
        visited[m] = visited[v] + 1
  # 정답 출력
  print(visited[M])
A, B, N, M = map(int,input().split())
# 탐색 시작
bfs()