n = int(input())

dp = [0] * (n + 1)
# 최소 연산을 하는 것이 목표
for i in range(2, n + 1):
  # 1로 뺀 경우
  dp[i] = dp[i-1] + 1
  # 2로 나누어지는 경우
  if i % 2 == 0:
    dp[i] = min(dp[i], dp[i//2] + 1)
  # 3으로 나누어지는 경우
  if i % 3 == 0:
    dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[n])