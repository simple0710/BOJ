# 2023/06/01 Math, DP
# https://www.acmicpc.net/problem/15624
N = int(input())
if N == 0: # 0인 경우
  print(0)
else: # 0이상인 경우
  dp = [0] * (N + 1)
  dp[1] = 1
  # 피보나치 구하기
  for i in range(2, N + 1): 
    dp[i] = (dp[i-1] + dp[i-2]) % 1000000007
  # 정답 출력
  print(dp[-1])