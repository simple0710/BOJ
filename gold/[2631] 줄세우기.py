# 2023/01/13 dp
# https://www.acmicpc.net/problem/2631
import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
  arr.append(int(input()))

# LIS 알고리즘
dp = [1] * N
for i in range(N):
  for j in range(i):
    if arr[j] < arr[i]:
      dp[i] = max(dp[j]+1, dp[i])

# 정답 출력
print(N - max(dp))