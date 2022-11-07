# 2022/11/01 너비우선탐색
from collections import deque
import sys
input = sys.stdin.readline

# 너비우선탐색
def bfs(v):
  visited = [False] * (N + 1)
  visited[v] = 0
  q = deque()
  q.append(v)
  while q:
    v = q.popleft()
    for pe in people[v]:
      # 방문하지 않은 경우 수행
      if type(visited[pe]) != int:
        visited[pe] = visited[v] + 1
        q.append(pe)
  # 합을 구한다.
  return sum(visited)

if __name__ == '__main__':
  # 정보 입력
  N, M = map(int,input().split())
  people = [[] for _ in range(N + 1)]
  for _ in range(M):
    a, b = map(int,input().split())
    people[a].append(b)
    people[b].append(a)

  # 케빈 베이컨의 6단계 시작_1
  ans = [0] * (N + 1)
  for i in range(1, N + 1):
    ans[i] = bfs(i)

  print(ans.index(min(ans[1:])))
  '''
  # 케빈 베이컨의 6단계 시작_2
  ans = []
  for i in range(1, N+1):
    ans.append(bfs(i))
  print(ans.index(min(ans)) + 1)
  '''