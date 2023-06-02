# 2023/05/28 Math, DP
# https://www.acmicpc.net/problem/10164
def search(sx, sy, ex, ey):
  for i in range(sx, ex):
    for j in range(sy, ey):
      if i == 0 or j == 0:
        dp[i][j] = 1
      else:
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

N, M, K = map(int,input().split())
dp = [[0] * M for _ in range(N)]
if K == 0:
  search(0, 0, N, M) # 끝까지 탐색
else:
  row = (K-1) // M
  col = (K-1) % M 
  search(0, 0, row + 1, col + 1) # 중간 지점까지 탐색
  search(row, col, N, M) # 중간부터 끝까지 탐색
# 정답 출력
print(dp[N-1][M-1])