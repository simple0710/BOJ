# 2022/11/14 BFS
from collections import deque
import sys
input = sys.stdin.readline

def bfs(a, b):
  # 최대로 나올 수 있는 값으로 visited 생성
  visited = [[False] * (total + 1) for _ in range(total + 1)]
  visited[a][b] = True
  q = deque()
  q.append((a, b))
  while q:
    x, y = q.popleft()
    # z는 최대에서 2개의 값은 뺀 값이다.
    z = total - x - y
    # 모두 같은 경우 1 반환
    if x == y == z:
      return 1
    # 2개의 그룹으로 나누어 계산(a가 작은 경우, b가 작은 경우, 같은 경우)
    for a, b in ((x, y), (y, z), (x, z)):
      if a < b:
        b -= a
        a += a
      elif a > b:
        a -= b
        b += b
      else:
        continue
      c = total - a - b
      # x, y 정의
      x = min(a, b, c)
      y = max(a, b, c)
      if not visited[x][y]:
        q.append((x, y))
        visited[x][y] = True
  return 0

# 정보 입력
a, b, c = map(int,input().split())
total = a + b + c 

# 3으로 나누어지지 않는다면 같아질 수 없다.
if total % 3 != 0:
  res = 0
else:
  res = bfs(a, b)

# 정답 출력
print(res)