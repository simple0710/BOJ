# 2023/05/18 Math, Implementation, BruteForce
# https://www.acmicpc.net/problem/1977
import math

M = math.ceil(int(input())**(1/2))
N = math.floor(int(input())**(1/2))

res = 0
res_min = M ** 2
# 완전제곱수 탐색
for i in range(M, N + 1):
  res += i ** 2
# 정답 출력
if res:
  print(res)
  print(res_min)
else:
  print(-1)