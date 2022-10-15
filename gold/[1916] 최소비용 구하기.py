import heapq
INF = int(1e9)

n = int(input())
m = int(input())

distance = [INF] * (n + 1)
bus = [[] for _ in range(n + 1)]

for _ in range(m):
  a, b, c = map(int,input().split())
  bus[a].append((b, c))
start, finish = map(int,input().split())

def dijkstra(start):
  q = []
  heapq.heappush(q,(0, start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in bus[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

dijkstra(start)

print(distance[finish])