import heapq
from itertools import combinations

n = int(input())
data = list(map(int,input().split()))
result = []
# nCi를 수행한다.
for i in range(1, n + 1):
  for j in combinations(data, i):
      heapq.heappush(result, sum(j))

i = 1
t = 0
answer = result[-1] + 1
while result:
  v = heapq.heappop(result)

  # 중복된 수 고려
  if t == v:
    continue
  t = v
  if i != v:
    answer = i
    break
  i += 1

print(answer)