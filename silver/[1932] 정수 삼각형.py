n = int(input())
data = [list(map(int,input().split())) for _ in range(n)]

for i in range(2, n + 1):
  for j in range(len(data[-i])):
    data[-i][j] += max(data[-i+1][j], data[-i+1][j+1])

print(*data[0])