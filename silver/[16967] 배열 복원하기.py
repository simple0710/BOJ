# 2023/04/23 Implementation
# https://www.acmicpc.net/problem/16967
H, W, X, Y = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(H + X)]
res = []
for i in range(H + X):
  check = []
  for j in range(W + Y):
    if i < X and j < W: # 앞부분
      check.append(data[i][j])
    elif i < H and j < W: # 뒷부분
      if i - X >= 0 and j - Y >= 0: # 겹치는 경우
        check.append(data[i][j] - res[i-X][j-Y])
      else: # 겹치지 않는 경우
        check.append(data[i][j])
  if check: # 배열 추가
    res.append(check)
for i in res: # 정답 출력
  print(*i)