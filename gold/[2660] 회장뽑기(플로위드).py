import sys
input = sys.stdin.readline
INF = int(1e9)

N = int(input())
data = list([INF] * (N + 1) for _ in range(N + 1))

while True:
  a, b = map(int,input().strip())
  if a == -1 and b == -1:
    break
  data[a][b] = 1
  data[b][a] = 1

for i in range(1, N + 1):
  data[i][i] = 0

for i in range(1, N + 1):
  for j in range(1, N + 1):
    for k in range(1, N + 1):
      if data[i][j] == 1 or data[i][j] == 0:
        continue
      if data[i][j] > data[i][k] + data[k][j]:
        data[i][j] = data[i][k] + data[k][j]

ans = []
for i in range(1, N + 1):
  ans.append(max(data[i][1:]))

score = min(ans)
print(score, ans.count(score))
for x, y in enumerate(ans):
  if y == score:
    print(x + 1, end= ' ')