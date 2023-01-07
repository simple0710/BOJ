# 2022/12/29 DP
# https://www.acmicpc.net/problem/15989
import sys
input = sys.stdin.readline
MAX = 10001

dp = [1] * MAX
# 2가 추가되는 경우
for i in range(2, MAX):
  dp[i] += dp[i-2]

# 3이 추가되는 경우
for i in range(3, MAX):
  dp[i] += dp[i-3]

T = int(input())
for _ in range(T):
  N = int(input())
  print(dp[N])