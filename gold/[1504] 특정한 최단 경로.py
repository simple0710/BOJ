# 2023/08/24 Dijkstra
# https://www.acmicpc.net/problem/1504
import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(N, graph, u):
  q = []
  heapq.heappush(q, (u, 0))
  distance = [INF] * (N + 1)
  distance[u] = 0
  while q:
    now, cost = heapq.heappop(q)
    # 현재 값이 비용보다 작은 경우
    if distance[now] < cost:
      continue
    for next, next_cost in graph[now]:
      nc = cost + next_cost # 비용 계산
      if nc < distance[next]:
        distance[next] = nc
        heapq.heappush(q, (next, nc))
  return distance

def solution(N, graph, u, v):
  # 1번 정정에서 시작
  o_distance = dijkstra(N, graph, 1)
  # u번 정점에서 시작
  u_distance = dijkstra(N, graph, u)
  # v번 정점에서 시작
  v_distance = dijkstra(N, graph, v)
  # 중간 두 지점을 포함한 거리
  path1 = o_distance[u] + u_distance[v] + v_distance[N]
  path2 = o_distance[v] + v_distance[u] + u_distance[N]

  res = min(path1, path2) # 최소 거리

  # 최단 정점이 있는 경우 거리 출력
  print(res if res < INF else -1)

def main():
  # 정점 개수, 간선 개수
  N, E = map(int,input().split())
  graph = [[] for _ in range(N + 1)]
  # 간선 정보
  for _ in range(E):
    a, b, c = map(int,input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
  # 지나야 하는 두 정점
  u, v = map(int,input().split())
  solution(N, graph, u, v) # 탐색 시작

if __name__ == "__main__":
  main()