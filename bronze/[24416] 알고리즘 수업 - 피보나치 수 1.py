# 2023/07/07 Math, DP
# https://www.acmicpc.net/problem/24416
N = int(input())
fibo = [1] * (N + 1)
for i in range(3, N + 1):
  fibo[i] = fibo[i-1] + fibo[i-2]
# 정답 출력
print(fibo[N], N - 2)