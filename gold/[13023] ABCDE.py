def dfs(v, d):
  global answer
  visited[v] = True
  # 4명이 관계가 있는 경우 answer = True
  if d == 4:
    answer = True
    return

  for i in data[v]:
    # 백트래킹
    if not visited[i]:
      visited[i] = True
      dfs(i, d + 1)
      visited[i] = False

# 데이터 입력
n, m = map(int,input().split())
data = [[] for _ in range(n)]
visited = [False] * n

for _ in range(m):
  a, b = map(int,input().split())
  data[a].append(b)
  data[b].append(a)

answer = False
# 관계 찾기
for i in range(n):
  dfs(i, 0)
  # 방문 처리 해제
  visited[i] = False
  # 정답이 있는 경우 종료
  if answer:
    break

# 출력
if answer:
  print(1)
else:
  print(0)