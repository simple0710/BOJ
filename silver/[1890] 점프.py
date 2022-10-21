n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
  for j in range(n):
    # 목적지에 도달했을 경우
    if i == n - 1 and j == n - 1:
      break
    # 해당 지역의 아래쪽과 오른쪽
    d = i + graph[i][j]
    r = j + graph[i][j]
    # 갈 수 있다면 이전 값과 원래 있던 값과 더한다.
    if d < n:
      dp[d][j] += dp[i][j]
    if r < n:
      dp[i][r] += dp[i][j]

print(dp[n-1][n-1])