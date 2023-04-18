# 2023/04/18 Math
# https://www.acmicpc.net/problem/1834
N = int(input())
res = 0
# 탐색 시작
for i in range(1, N):
  res += N * i + i
# 정답 출력
print(res)