# 2023/12/06 Dijkstra
# https://www.acmicpc.net/problem/18223
import heapq
INF = int(1e9)

def dijkstra(start):
  q = [(start, 0)]
  distance = [INF] * (V + 1)
  distance[start] = 0
  while q:
    now, now_cost = heapq.heappop(q)
    if distance[now] < now_cost:
      continue
    for next, next_cost in graph[now]:
      # 다음 비용 확인
      total_cost = now_cost + next_cost
      if distance[next] > total_cost: # 거리가 더 작다면 갱신
        distance[next] = total_cost
        heapq.heappush(q, (next, total_cost))
  return distance # 거리 결과 반환
    
def main():
  global V, graph
  V, E, P = map(int,input().split())
  graph = [[] for _ in range(V+1)]
  for _ in range(E):
    a, b, c = map(int,input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
  # 1에서 시작한 뒤 거리의 결과
  default_distance = dijkstra(1)
  # P에서 시작한 뒤 거리의 결과
  P_distance = dijkstra(P)
  # 두 거리가 같다면 구할 수 있다.
  if default_distance[V] == default_distance[P] + P_distance[V]:
    print('SAVE HIM')
  else:
    print('GOOD BYE')

if __name__ == "__main__":
  main()