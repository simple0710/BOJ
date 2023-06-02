# 2023/05/26 Math, DP
# https://www.acmicpc.net/problem/16395
N, K = map(int,input().split())
dp = []
for i in range(N):
  row = []
  for j in range(i + 1):
    check = 1
    if j != 0 and j != i: # 끝부분이 아닌 경우
      check = dp[i-1][j-1] + dp[i-1][j]
    row.append(check) # 행에 값 추가
  dp.append(row) # 행 추가
# N번째 행, K번째 값 출력
print(dp[N-1][K-1])