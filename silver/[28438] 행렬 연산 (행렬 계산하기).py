# 2023/08/07 Math, Implementation
# https://www.acmicpc.net/problem/28438
import sys
input = sys.stdin.readline

N, M, Q = map(int,input().split())
data = [[0] * (M + 1) for _ in range(N + 1)]
for _ in range(Q):
  t, x, u = map(int,input().split())
  # 각 행, 열에 해당하는 첫 부분에 값을 저장해 둔다.
  if t == 1:
    data[x][0] += u
  else:
    data[0][x] += u
# 나머지 칸에 저장
for i in range(1, N + 1):
  for j in range(1, M + 1):
    data[i][j] = data[0][j] + data[i][0]
  # 정답 출력
  print(*data[i][1:])