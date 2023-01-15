# 2023/01/13 DFS
# https://www.acmicpc.net/problem/9466
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

# 깊이우선탐색
def dfs(v):
  global res
  c.append(v)
  visited[v] = True
  num = arr[v-1]
  if visited[num]:
    # 사이클이 돈 경우
    if num in c:
      # 이어붙이기
      # c.index(num) : 1, 3, 3의 순서로 접근한 경우 3 혼자만 팀이 되기 때문이다.
      res += c[c.index(num):]
    return
  else:
    dfs(num)

for _ in range(int(input())):
  N = int(input())
  arr = list(map(int,input().split()))
  visited = [False] * (N+1)
  res = [] # 팀에 속한 사람 수
  for i in range(1, N+1):
    if not visited[i]:
      c = [] # 사이클
      dfs(i) # 탐색 시작

  # 정답 출력
  print(N-len(res))