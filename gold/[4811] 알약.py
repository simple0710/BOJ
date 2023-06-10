# 2023/06/10 Math, DP
# https://www.acmicpc.net/problem/4811
dp = [[0] * 31 for _ in range(31)]
# i : 한조각의 수 (W)
# j : 반조각의 수 (H)
for i in range(1, 31):
  dp[0][1] = 1
# 탐색 시작
for i in range(1, 31):
  for j in range(i, 31):
    dp[i][j] += dp[i-1][j] + dp[i][j-1]
while True:
  N = int(input())
  if N == 0: # 종료
    break
  # 정답 출력
  print(dp[N][N])