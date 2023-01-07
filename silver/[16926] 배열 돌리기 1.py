# 2022/12/08 구현
# https://www.acmicpc.net/problem/16926
import sys
input = sys.stdin.readline

N, M, R = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(N)]

for _ in range(R):
  for i in range(min(N, M) // 2):
    x, y = i, i
    tmp = data[x][y]
    for j in range(i + 1, N - i): # 상
      x = j
      prev_value = data[x][y]
      data[x][y] = tmp
      tmp = prev_value
    
    for j in range(i + 1, M - i): # 좌
      y = j
      prev_value = data[x][y]
      data[x][y] = tmp
      tmp = prev_value
    
    for j in range(i + 1, N - i): # 하
      x = N - j - 1
      prev_value = data[x][y]
      data[x][y] = tmp
      tmp = prev_value

    for j in range(i + 1, M - i): # 우
      y = M - j - 1
      prev_value = data[x][y]
      data[x][y] = tmp
      tmp = prev_value

for i in data:
  print(' '.join(map(str, i)))