# 무게, 가중치
n, k = map(int,input().split())

data = [[0, 0]]
for i in range(n):
  data.append(list(map(int,input().split())))

dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
  for j in range(1, k + 1):
    # 현재 선택한 물건 스펙
    w = data[i][0]
    v = data[i][1]
    # 하용범위가 작은 경우는 넣지 않는다.
    # 해당 물건의 무게 인덱스에 v값을 넣는다.
    if j < w:
      dp[i][j] = dp[i-1][j]
    # 물건을 넣는다.
    # j-w 는 dp[현재 배낭 - 현재 물건의 무게] + v
    else:
      dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)

print(dp[n][k])
'''
n, k = map(int,input().split())

data = [[0,0]]
for _ in range(n):
  data.append(list(map(int,input().split())))

dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
  for j in range(1, k + 1):
    w = data[i][0]
    v = data[i][1]
    if j < w:
      dp[i][j] = dp[i-1][j]
    else:
      dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)
print(dp[n][k])
'''