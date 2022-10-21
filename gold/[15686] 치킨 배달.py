from itertools import combinations
import sys
input = sys.stdin.readline
INF = int(1e9)

def solution():
  result = INF
  for ch in combinations(c, m):
    print(ch)
    tmp = 0
    for a, b in h:
      dist = INF
      for x, y in ch:
        dist = min(dist, (abs(a - x) + abs(b - y)))
      tmp += dist
    result = min(result, tmp)
  print(result)

n, m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

h = []
c = []
for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
      h.append((i, j))
    if graph[i][j] == 2:
      c.append((i, j))

solution()