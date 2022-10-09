import sys
import heapq
INF = int(1e9)
input = sys.stdin.readline

def dijkstra(start):
  distance = [INF] * (n + 1)

  q = []
  heapq.heappush(q,(0, start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for node_index, node_cost in graph[now]:
      cost = dist + node_cost
      if cost < distance[node_index]:
        distance[node_index] = cost
        heapq.heappush(q, (cost, node_index))

  return distance
n, m, x = map(int,input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
  a, b, c = map(int,input().split())
  graph[a].append((b, c))

result = 0
for i in range(1, n + 1):
  go = dijkstra(i)
  back = dijkstra(x)
  result = max(result, go[x] + back[i])

print(result)