# 2022/12/25 DP
# https://www.acmicpc.net/problem/11055
N = int(input())
data = list(map(int,input().split()))
dp = [0] * N
for i in range(N):
  dp[i] = data[i] # 값 지정
  for j in range(i):
    # 만약 자신보다 작다면 비교한다.
    if data[i] > data[j]:
      dp[i] = max(dp[j] + data[i], dp[i])
# 정답 출력
print(max(dp))