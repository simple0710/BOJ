# 2023/02/05 BFS
# https://www.acmicpc.net/problem/18232
from collections import deque
import sys
input = sys.stdin.readline

def bfs(x):
  q = deque([x])
  visited = [False] * (N+1)
  visited[x] = 1
  while q:
    v = q.popleft()
    if v == E: # 목적지에 도달한 경우
      return visited[v] - 1
    for i in (v-1, v+1): # 한칸씩 이동
      if 1 <= i <= N and not visited[i]:
        q.append(i)
        visited[i] = visited[v] + 1

    if v in warp.keys(): # 해당 구역 워프 확인
      for j in warp[v]:
        if not visited[j]:
          q.append(j)
          visited[j] = visited[v] + 1

N, M = map(int,input().split())
S, E = map(int,input().split())
warp = dict() # 리스트로 구현 가능하다.
for _ in range(M):
  a, b = map(int,input().split())
  if a not in warp.keys():
    warp[a] = set([b])
  else:
    warp[a].add(b)
  if b not in warp.keys():
    warp[b] = set([a])
  else:
    warp[b].add(a)
  
# 탐색 시작
res = bfs(S)

# 정답 출력
print(res)