# 2022/11/21 DP
N = int(input())

# 리스트 생성
dp = [[0] * 10 for _ in range(N + 1)]
# 1자리 수에 1~9까지 1로 지정, 0은 세지 않는다.
for i in range(1, 10):
  dp[1][i] = 1

MOD = 1000000000
for i in range(2, N+1):
  for j in range(10):
    if j == 0:
      dp[i][j] = dp[i-1][1]
    elif j == 9:
      dp[i][j] = dp[i-1][8]
    # dp[자리 수][뒤의 수] = dp[자리 수 - 1][뒤의 수 - 1] + dp[자리 수 - 1][뒤의 수 + 1]
    else:
      dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
# 정답 출력
print(sum(dp[N]) % MOD)