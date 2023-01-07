# 2022/12/27 DP
# https://www.acmicpc.net/problem/13398
N = int(input())
data = list(map(int,input().split()))
# 원래의 합과 하나를 뺀 합
dp = [[0] * N for _ in range(2)]
dp[0][0] = data[0]
if N > 1:
  res = -int(1e9)
  for i in range(1, N):
    dp[0][i] = max(dp[0][i-1] + data[i], data[i]) # 그냥 합
    dp[1][i] = max(dp[0][i-1], dp[1][i-1] + data[i]) # 하나를 뺀 합
    res = max(res, dp[0][i], dp[1][i]) # 정답 갱신
else:
  res = data[0]

# 정답 출력
print(res)
