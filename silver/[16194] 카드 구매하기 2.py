# 2022/11/13 다이나믹 프로그래밍
N = int(input())
data = [0] + list(map(int,input().split()))
dp = [False] * (N + 1)

for i in range(1, N + 1):
  for j in range(1, i + 1):
    # 값이 아직 채워지지 않은 경우
    if dp[i] == False:
      dp[i] = dp[i-j] + data[j]
    else:
      dp[i] = min(dp[i], dp[i-j] + data[j])
      
print(dp[N])