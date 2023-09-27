# 2023/09/27 DFS, BFS
# https://www.acmicpc.net/problem/16947
from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(v, rotation): # 순환 확인
  for i in graph[v]:
    if visited[i] == -1:
      visited[i] = 0
      dfs(i, rotation+[i])
    else:
      # 3구간 이상인 경우, 순환하는 경우
      if len(rotation) >= 3 and i == rotation[0]:
          print(bfs(rotation)) # 각 역과 순환선 사이의 거리 출력
          sys.exit(0)

def bfs(rotation): # 각 역과 순환선 사이의 거리 출력
  res = [-1] * (N+1)
  for i in rotation:
    res[i] = 0
  q = deque([i for i in rotation])
  while q:
    v = q.popleft()
    for i in graph[v]:
      if res[i] == -1:
        res[i] = res[v] + 1
        q.append(i)
  return ' '.join(map(str, res[1:])) # 정답 반환

def solution():
  global visited

  for now in range(1, N+1):
    visited = [-1] * (N+1)
    visited[now] = 0
    dfs(now, [now]) # 순환 여부 확인 시작

def main():
  global N, graph

  N = int(input())
  graph = [[] for _ in range(N+1)]
  for _ in range(N):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
  solution() # 코드 실행

if __name__ == "__main__":
  main()