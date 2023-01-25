# 2023/01/25 DP
# https://www.acmicpc.net/problem/1915
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
dp = [[0] * M for _ in range(N)]
data = []
res = 0
for i in range(N):
  data.append(list(input().rstrip()))
  for j in range(M):
    if data[i][j] == '1':
      dp[i][j] = 1
      res = 1
# 탐색 시작
for i in range(1, N):
  for j in range(1, M):
    if data[i][j] == '1':
      # 해당칸 주변이 1인 경우 + 최소 값과 현재 위치의 값을 더한다.
      dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + dp[i][j]
      res = max(res, dp[i][j]) # 최대 값 저장
# 정답 출력
print(res**2)