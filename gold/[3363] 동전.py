# 2023/02/04 DP
# https://www.acmicpc.net/problem/9084
T = int(input())
for _ in range(T):
  N = int(input())
  arr = list(map(int,input().split()))
  M = int(input())
  dp = [0] * (M+1)
  dp[0] = 1
  for i in arr:
    for j in range(i, M + 1):
      dp[j] += dp[j - i] # 현재 단위를 뺀 값으로 만든 금액의 경우의 수를 더한다.
  # 정답 출력
  print(dp[M])