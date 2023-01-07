# 2022/12/24 DP
# https://www.acmicpc.net/problem/2133
N = int(input())

dp = [0] * (N + 2)
dp[2] = 3
# 이전 값에서 3개 모양을 추가하므로 dp[i-2] * 3
# 3X4을 다 채우는 특수한 모양을 이용한 방법 2 * dp[j]
# 3XN을 다 채우는 도형 2개
for i in range(4, N + 1, 2):
  dp[i] = dp[i-2] * 3
  for j in range(i-4, -1, -2):
    dp[i] += 2 * dp[j]
  dp[i] += 2

# 정답 출력
print(dp[N])