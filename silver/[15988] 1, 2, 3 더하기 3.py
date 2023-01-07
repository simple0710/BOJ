# 2022/12/23 DP
# https://www.acmicpc.net/problem/15988
import sys
input = sys.stdin.readline

dp = [0] * 1000001
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, 1000001):
  # 이전 세개의 합
  dp[i] = (dp[i-3] + dp[i-2] + dp[i-1]) % 1000000009

T = int(input())
for _ in range(T):
  N = int(input())
  print(dp[N])