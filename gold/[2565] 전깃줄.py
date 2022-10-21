data = list()
t = int(input())
for _ in range(t):
  x, y = map(int,input().split())
  data.append((x, y))

# 2번째 전깃줄 기준으로 한 data 정렬
data.sort(key = lambda x:x[1])
print(data)
dp = [1] * t

# 설치한 전깃줄의 수 (LIS 알고리즘)
for i in range(1, t):
  for j in range(i):
    if data[i] > data[j]:
      dp[i] = max(dp[i], dp[j] + 1)

print(t - max(dp))
print(t - max(dp))