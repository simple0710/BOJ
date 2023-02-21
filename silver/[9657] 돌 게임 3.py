# 2023/02/20 DP
# https://www.acmicpc.net/problem/9657
N = int(input())
dp = [0] * 1001
dp[1] = 1
dp[3] = 1
dp[4] = 1
for i in range(5, N+1):
  # 이전에 상대가 돌을 둔 경우
  if not dp[i-1]:
    dp[i] = 1
  # i-3번째에 상대가 돌을 둔 경우
  if not dp[i-3]:
    dp[i] = 1
  # i-4번째에 상대가 돌을 둔 경우
  if not dp[i-4]:
    dp[i] = 1

# 해당 위치에 돌이 있으면 SK 출력
if dp[N]:
  print("SK")
# 해당 위치에 돌이 없으면 CY 출력
else:
  print("CY")