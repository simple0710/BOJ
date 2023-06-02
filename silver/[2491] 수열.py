# 2023/05/30 Implementation, DP
# https://www.acmicpc.net/problem/2491
N = int(input())
data = list(map(int,input().split()))
dp = [[1] * N for _ in range(2)]
for i in range(1, N):
  if data[i] >= data[i-1]: # 증가하거나 같은 수열인 경우
    dp[0][i] = dp[0][i-1] + 1
  if data[i] <= data[i-1]: # 감소하거나 같은 수열인 경우
    dp[1][i] = dp[1][i-1] + 1
# 정답 출력
print(max(max(dp[0]), max(dp[1])))