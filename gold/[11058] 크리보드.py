# 2022/12/30 DP
# https://www.acmicpc.net/problem/11058
import sys
imput = sys.stdin.readline

N = int(input())
dp = [i for i in range(N + 1)]
for i in range(7, N+1):
  # v를 한 번, 두 번, 세 번 누른 경우
  # 값은 각각 2배, 3배, 4배가 된다.
  dp[i] = max(dp[i-3] * 2, dp[i-4] * 3, dp[i-5] * 4)

# 정답 출력
print(dp[N])