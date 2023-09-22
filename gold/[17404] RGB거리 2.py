# 2023/07/31 DP
# https://www.acmicpc.net/problem/17404
MAX = 1000 ** 2 + 1

N = int(input())
house = [list(map(int,input().split())) for _ in range(N)]
dp = [[[MAX] * 3 for _ in range(N)] for _ in range(3)]
# 맨 처음 칠하는 집의 위치, 현재 순서, 색깔
dp[0][0][0] = house[0][0]
dp[1][0][1] = house[0][1]
dp[2][0][2] = house[0][2]
for i in range(1, N):
  for s in range(3):
    dp[s][i][0] = house[i][0] + min(dp[s][i-1][1], dp[s][i-1][2])
    dp[s][i][1] = house[i][1] + min(dp[s][i-1][0], dp[s][i-1][2])
    dp[s][i][2] = house[i][2] + min(dp[s][i-1][0], dp[s][i-1][1])

# 최솟값 구하기
res = MAX - 1
for i in range(3):
  for j in range(3):
    if i != j:
      res =  min(res, dp[i][-1][j])

# 정답 출력
print(res)