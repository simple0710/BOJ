# 2023/05/21 DP
# https://www.acmicpc.net/problem/1495
N, S, M = map(int,input().split())
data = [0] + list(map(int,input().split()))
dp = [[-1] * (M + 1) for _ in range(N + 1)]
dp[0][S] = S # 시작 지점
for i in range(1, N + 1):
  for j in range(M + 1):
    if dp[i-1][j] >= 0: # 이전에 연주할 수 있는 경우
      up = j + data[i]
      down = j - data[i]
      # 범위 안에 있으면 값 지정
      if up <= M:
        dp[i][up] = up
      if down >= 0:
        dp[i][down] = down
  if sum(dp[i]) == -(M + 1): # 연주하지 못한 경우 -1 출력
    print(-1)
    break
else: # 연주에 성공한 경우, 연주 가능한 볼륨의 최댓값 출력
  print(max(dp[-1]))