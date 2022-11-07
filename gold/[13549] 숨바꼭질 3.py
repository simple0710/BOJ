# 2022/10/31 너비우선탐색
from collections import deque
import sys
input = sys.stdin.readline
MAX = int(1e5) + 1

def bfs(v, k):
  visited = [0] * MAX
  # 순간이동만 했을 경우를 대비한다
  visited[v] = 1
  q = deque([v])
  while q:
    v = q.popleft()
    if v == k:
      return visited[k] - 1
    # 움직일 수 있는 경로
    for move in [v*2, v-1, v+1]:
      if 0 <= move < MAX and not visited[move]:
        # 순간이동한 경우엔 바로 다시 수행한다.
        if move == v*2:
          visited[move] = visited[v]
          q.appendleft(move)
        else:
          visited[move] = visited[v] + 1
          q.append(move)

n, k  = map(int,input().split())
print(bfs(n, k))