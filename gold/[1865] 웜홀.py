# 2023/08/26 Bellman-Ford
# https://www.acmicpc.net/problem/1865
import sys
input = sys.stdin.readline
INF = int(1e9)

def bellman_ford(v):
  distance = [INF] * (N + 1)
  distance[v] = 0
  for i in range(N): # N번 반복
    for s, e, t in graph: # 모든 간선 확인
      if distance[e] > distance[s] + t:
        if i == N - 1: # N번째 라운드에서도 값이 갱신된다면 음수 순환이 존재한다.
          return True
        distance[e] = distance[s] + t
  return False

if __name__ == "__main__":
  T = int(input())
  for _ in range(T):
    N, M, W = map(int,input().split())
    graph = []
    for _ in range(M):
      S, E, T = map(int,input().split())
      graph.append((S, E, T))
      graph.append((E, S, T))
    for _ in range(W):
      S, E, T = map(int,input().split())
      graph.append((S, E, -T))

    if bellman_ford(1): # 음수 순환이 존재하는 경우
      print("YES")
    else: # 음수 순환이 존재하지 않는 경우
      print("NO")