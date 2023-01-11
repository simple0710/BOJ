# 2023/01/11 dp
# https://www.acmicpc.net/problem/9461
import sys
input = sys.stdin.readline
MAX = 100

dp = [0] * (MAX + 1)
dp[1] = 1
dp[2] = 1
dp[3] = 1
for i in range(4, MAX + 1):
  dp[i] = dp[i-3] + dp[i-2] 

for _ in range(int(input())):
  N = int(input())
  # 정답 출력
  print(dp[N])