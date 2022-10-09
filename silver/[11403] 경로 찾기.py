n = int(input())

graph = [list(map(int,input().split())) for _ in range(n)]

# a에서 b로 갈 때 거쳐가는 교차점
for k in range(n):
  for a in range(n):
    for b in range(n):
      # ex) 0, 0이 체크된 경우는 0 - 1 - 0 같은 경우
      if graph[a][k] and graph[k][b]:
        graph[a][b] = 1

for a in range(n):
  for b in range(n):
    print(graph[a][b], end = ' ')
  print()