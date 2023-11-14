# 2023/07/29 BFS
# https://www.acmicpc.net/problem/18352
from collections import deque
import sys
input = sys.stdin.readline

def bfs():
  q = deque([X])
  visited = [-1] * (N + 1)
  visited[X] = 0
  while q:
    now = q.popleft()
    for next in city_root[now]:
      if visited[next] == -1: # 아직 방문하지 않은 경우
        q.append(next)
        visited[next] = visited[now] + 1
  flag = False
  for index, x in enumerate(visited):
    if x == K: # 거리가 K인 경우 출력
      print(index)
      flag = True
  if not flag: # K인 경우가 없는 경우
    print(-1)

# N: 출발 지역
# M: 도로의 개수
# K: 거리 정보
# X: 출발 도시 정보 
N, M, K, X = map(int,input().split())
# 단방향 도로 정보
city_root = [[] for _ in range(N + 1)]
for _ in range(M):
  a, b = map(int,input().split())
  city_root[a].append(b)
# 탐색 시작
bfs()