n = int(input())
data = [0] + list(map(int,input().split()))
dp = [0] * (n+1)

# 점화식 : dp[i] = dp[i-k] + data[k]
# i는 산 카드의 수
# k는 들어있는 카드팩
for i in range(1, n+1):
  for k in range(1, i+1):
    dp[i] = max(dp[i], dp[i-k] + data[k])
print(dp[n])
