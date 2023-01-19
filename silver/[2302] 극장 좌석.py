# 2023/01/19 DP
# https://www.acmicpc.net/problem/2302
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
data = list(int(input()) for _ in range(M))

dp = [0] * 41
dp[0] = 1
dp[1] = 1
dp[2] = 2
for i in range(3, N+1):
  dp[i] = dp[i-2] + dp[i-1]

res = 1
# 지정석이 있는 경우
if M > 0:
  # 각 구역에 나올 수 있는 경우의 수를 곱한 합
  p = 0
  for i in range(M):
    res *= dp[data[i] - 1 - p] # 3 - 1 - 0, 7 - 1 - 3
    p =  data[i]
  res *= dp[N - p]
# 지정석이 없는 경우
else:
  res = dp[N]

# 정답 출력
print(res)