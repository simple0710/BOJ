# 2023/04/18 Math
# https://www.acmicpc.net/problem/1834
N = int(input())
res = 0
i = 1
# 탐색 시작
while i // N <= i % N:
  res += (N + 1) * i
  i += 1
# 정답 출력
print(res)