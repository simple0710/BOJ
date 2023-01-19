# 2023/01/18 DP
# https://www.acmicpc.net/problem/14925
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
dp = [[0] * (M+1) for _ in range(N+1)]
data = [list(map(int,input().split())) for _ in range(N)]
res = 0
for i in range(1, N+1):
  for j in range(1, M+1):
    if not data[i-1][j-1]: # 들판이 나오면 0부터 시작
      dp[i][j] = min(dp[i-1][j], dp[i][j-1], data[i-1][j-1]) + 1
      res = max(dp[i][j], res)
# 정답 출력
print(res)