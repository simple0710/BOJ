# 2023/01/05 DP
# https://www.acmicpc.net/problem/2579
import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)] + [0, 0]
dp = [0] * (N + 2)
dp[0] = arr[0]
dp[1] = arr[0] + arr[1]
dp[2] = max(dp[0], arr[1]) + arr[2]

for i in range(3, N):
  # 현재 칸에서 i-2 칸을 밟은 값 vs i-1칸을 밟은 값
  dp[i] = arr[i] + max(dp[i-2], arr[i-1] + dp[i-3])

# 정답 출력
print(dp[N-1])