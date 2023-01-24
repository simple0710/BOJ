# 2023/01/20 DP
# https://www.acmicpc.net/problem/12852
import sys
input = sys.stdin.readline

N = int(input())
dp = [[0, []] for _ in range(N + 1)] # 경우의 수, 경로
dp[1][0] = 0
dp[1][1] = [1]
for i in range(2, N + 1):
  # 1을 뺀 경우
  dp[i][0] = dp[i-1][0] + 1
  dp[i][1] = dp[i-1][1] + [i]
  if i % 3 == 0 and dp[i//3][0] + 1 < dp[i][0]: # 3으로 나누어지고 더 짧은 경로인 경우
    dp[i][0] = dp[i//3][0] + 1
    dp[i][1] = dp[i//3][1] + [i]
  if i % 2 == 0 and dp[i//2][0] + 1 < dp[i][0]: # 2로 나누어지고 더 짧은 경로인 경우
    dp[i][0] = dp[i//2][0] + 1
    dp[i][1] = dp[i//2][1] + [i]

# 정답 출력
print(dp[N][0])
for i in dp[N][1][::-1]:
  print(i, end=' ')