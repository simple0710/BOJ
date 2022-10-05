n = int(input())

data = list(map(int,input().split()))

# 0부터 20의 리스트를 n개 만든다.
dp = [[0] * 21 for _ in range(n)] 
# 맨 처음 값은 해당 인덱스에 +1을 한다.
dp[0][data[0]] += 1

# 마지막은 결과값이다.
for i in range(1,n-1):
  # 이전 결과에서 나올 수 있는 값에 계산을 수행한다.
  for j in range(21):
    if dp[i-1][j]:
      # 그 값이 범위 내에 있다면 연산 전의 값 + 현재 경우의 수를 수행한다.
      if j + data[i] <= 20:
        dp[i][j + data[i]] += dp[i-1][j]
      if j - data[i] >= 0:
        dp[i][j - data[i]] += dp[i-1][j]

# 마지막 값이 결과값인걸 감안한다.
print(dp[n-2][data[n-1]])