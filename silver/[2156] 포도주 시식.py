n = int(input())
data = list()
dp = [0] * n

for i in range(n):
  data.append(int(input()))

if n < 3:
  print(sum(data))
# 포도주 먹는 3가지 방법
# 1. 1번째와 3번째를 먹는 방법 
# 2. 2번째와 3번째를 먹는 방법 
# 3. 현재 먹는걸 안 먹는 방법
else:
  dp[0] = data[0]
  dp[1] = data[0] + data[1]
  dp[2] = max(data[0] + data[2], data[1] + data[2], dp[1])
  for i in range(3, n):
    # 1 3을 먹는 경우, 0 2 3 을 먹는 경우, 안 먹는 경우
    dp[i] = max(dp[i-2] + data[i], dp[i-3] + data[i-1] + data[i], dp[i-1])

  print(max(dp))
