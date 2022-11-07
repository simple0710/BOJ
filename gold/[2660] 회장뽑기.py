# 2022/10/30
from collections import deque
import sys
input = sys.stdin.readline

# 너비우선탐색
def bfs(v):
  q = deque()
  q.append(v)
  visited = [-1] * (N + 1)
  visited[v] = 0
  while q:
    v = q.popleft()
    for i in data[v]:
      # 아직 방문하지 않았다면 i값에 v + 1 
      if visited[i] == -1:
        visited[i] = visited[v] + 1
        q.append(i)
  # 가장 큰 점수를 출력한다
  return max(visited)

N = int(input())
data = list([] for _ in range(N + 1))

while True:
  a, b = map(int,input().split())
  if a == -1 and b == -1:
    break
  data[a].append(b)
  data[b].append(a)

score = 50
ans = []
for i in range(1, N + 1):
  tmp = bfs(i)
  # tmp가 socore 보다 작다면 값 변경
  if tmp < score:
    score = tmp
    ans = [i]
  # 같은 값은 추가
  elif tmp == score:
    ans.append(i)

# 출력
print(score, len(ans))
print(*ans)