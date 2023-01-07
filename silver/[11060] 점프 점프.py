# 2022/12/29 DP
# https://www.acmicpc.net/problem/11060
import sys
input = sys.stdin.readline
MAX = int(1e9)

N = int(input())
arr = list(map(int,input().split()))
dp = [MAX] * N
dp[0] = 0
for i in range(N):
  # 현재 위치에서 점프할 수 있는 영역 확인
  for j in range(i+1, i + arr[i] + 1):
    if j == N:
      break
    dp[j] = min(dp[i] + 1, dp[j])

# 목적지에 도달하지 못한 경우 -1 출력
if dp[N-1] == MAX:
  print(-1)
# 목적지에 도달한 경우 점프 수 출력
else:
  print(dp[N-1])