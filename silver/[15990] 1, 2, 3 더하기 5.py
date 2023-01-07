# 2022/12/09 DP
# https://www.acmicpc.net/problem/15990
import sys
input = sys.stdin.readline

dp = [[0] * 3 for _ in range(100001)]
# 해당 수로 끝나는 dp 생성
dp[1] = [1, 0, 0]
dp[2] = [0, 1, 0]
dp[3] = [1, 1, 1]
# i 인 경우
for i in range(4, 100001):
  # i - 1 에서 2 or 3으로 끝난 값에 1 붙이기
  dp[i][0] = dp[i-1][1] % 1000000009 + dp[i-1][2] % 1000000009
  # i - 2 에서 1 or 3으로 끝난 값에 2 붙이기
  dp[i][1] = dp[i-2][0] % 1000000009 + dp[i-2][2] % 1000000009
  # i - 3 에서 1 or 2로 끝난 값에 3 붙이기
  dp[i][2] = dp[i-3][0] % 1000000009 + dp[i-3][1] % 1000000009

for _ in range(int(input())):
  n = int(input())
  print(sum(dp[n]) % 1000000009)