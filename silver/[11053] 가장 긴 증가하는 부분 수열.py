t = int(input())
data = list(map(int,input().split()))

dp = [1 for i in range(t)]

# 자신보다 큰 수가 나올 경우 dp를 비교해서 큰 값을 저장한다.
for i in range(t):
  for j in range(i):
    if data[i] > data[j]:
      dp[i] = max(dp[i], dp[j]+1)
print(max(dp))