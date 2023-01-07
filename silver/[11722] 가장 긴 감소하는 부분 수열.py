# 2022/12/25 DP
# https://www.acmicpc.net/problem/11722
N = int(input())
data = list(map(int,input().split()))
dp = [1] * N
for i in range(N):
  for j in range(i):
    # 자신보다 큰 값인 경우 비교
    if data[i] < data[j]:
      dp[i] = max(dp[j] + 1, dp[i])
# 정답 출력
print(max(dp))