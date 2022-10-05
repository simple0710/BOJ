INF = int(1e9) # 100001로 설정하면 98%에서 틀린다

n = int(input())
m = int(input())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(m):
  a, b, c = map(int,input().split())
  # 같은 길을 가는 버스가 두 대인 경우
  graph[a][b] = min(graph[a][b], c)

# k는 거쳐가는 노드, a는 출발하는 노드, b는 도착하는 노드
for k in range(1, n + 1):
  for a in range(1, n + 1):
    for b in range(1, n + 1):
      if a == b:
        graph[a][b] = 0
      else:
        graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 출력
for a in range(1, n + 1):
  for b in range(1, n + 1):
    # 가는 길이 없는 경우 0으로 표현
    if graph[a][b] == INF:
      print(0, end = " ")
    else:
      print(graph[a][b], end = " ")
  print()
'''
for i in range(1, n+1):
  print(' '.join(map(str,graph[i][1:])))
'''