# 2023/01/11 DP
# https://www.acmicpc.net/problem/1965
N = int(input())
arr = list(map(int,input().split()))
dp = [1] * N
for i in range(N):
  for j in range(i):
    # 크기가 작다면 비교
    if arr[i] > arr[j]:
      dp[i] = max(dp[i], dp[j] + 1)
# 정답 출력
print(max(dp))
