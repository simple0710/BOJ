# 2023/05/29 DP, LIS
# https://www.acmicpc.net/problem/18353
N = int(input())
data = list(map(int,input().split()))
dp = [1] * (N)
for i in range(N):
  for j in range(i):
    if data[i] < data[j]: # 현재 값이 data[j]보다 작은 경우
      dp[i] = max(dp[i], dp[j] + 1)
# 정답 출력
print(N - max(dp))
