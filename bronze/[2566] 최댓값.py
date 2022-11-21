res = -1
data = []
for i in range(9):
  data.append(list(map(int,input().split())))
  for j in range(9):
    if data[i][j] > res:
      res = data[i][j]
      x, y = i, j
print(res)
print(x-1, y-1)
