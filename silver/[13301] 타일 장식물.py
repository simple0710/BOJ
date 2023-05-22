# 2023/05/22 Math, DP
# https://www.acmicpc.net/problem/13301
N = int(input())
dp = [0] * (N + 1)
dp[1] = 1
row = 1
col = 1
for i in range(2, N + 1):
  dp[i] = dp[i-1] + dp[i-2]
  if i % 2 == 0: # 짝수인 경우 행의 값 증가
    row += dp[i]
  else: # 홀수인 경우 열의 값 증가
    col += dp[i]
# 정답 출력
print(2 * (row + col))