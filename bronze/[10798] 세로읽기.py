# 2023/04/03 Implementation, String
# https://www.acmicpc.net/problem/10798
data = [list(input()) for _ in range(5)]

for i in range(15): # 열
  for j in range(5): # 행
    if len(data[j]) <= i:
      continue
    # 정답 출력
    print(data[j][i], end = '')