# 2022/11/05 깊이우선탐색, 이분그래프
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

# 깊이 우선 탐색
def dfs(v, c):
  # 해당 색으로 지정한다 (-1, 1)
  visited[v] = c
  for i in data[v]:
    if not visited[i]:
      a = dfs(i, -c)
      if not a:
        return False
    elif visited[v] == visited[i]:
      return False
  return True

# 다른 방법(깔끔)
'''
def dfs(v, c):
  global err

  if err:
    return

  visited[v] = c
  for i in data[v]:
    if not visited[i]:
      dfs(i, -c)
    elif visited[v] == visited[i]:
      err = True
      return
'''
for _ in range(int(input())):
  # 정점의 수 및 간선의 수 입력
  V, E = map(int,input().split())
  # 데이터 입력
  data = [[] for _ in range(V + 1)]
  visited = [False] * (V + 1)
  for _ in range(E):
    x, y = map(int,input().split())
    data[x].append(y)
    data[y].append(x)

  # 탐색 시작
  for i in range(1, V + 1):
    if not visited[i]:
      res = dfs(i, 1)
      if not res:
        break
  # 정답 출력
  if res:
    print("YES")
  else:
    print("NO")
