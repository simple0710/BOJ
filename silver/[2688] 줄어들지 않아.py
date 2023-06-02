# 2023/05/27 DP
# https://www.acmicpc.net/problem/2688
for _ in range(int(input())):
  N = int(input()) + 1
  dp = [[0] * (10) for _ in range(N)]
  for i in range(10): # 0번째 값
    dp[0][i] = 1
  for turn in range(1, N):
    for now_num in range(10): # 각 숫자에 대해 이전 턴의 값과, 현재 턴의 값을 더한다.
      dp[turn][now_num] = dp[turn - 1][now_num] + (dp[turn][now_num - 1] if now_num else 0)
  # 정답 출력
  print(dp[-1][-1])