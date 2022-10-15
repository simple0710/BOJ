# 백트래킹 접근(실패, 시간초과)
'''
def back():
  global result
  if sum(s) == k and len(s) == n:
    result += 1
    return
  elif len(s) > n:
    return 
  for i in range(len(data)):
    s.append(data[i])
    back()
    s.pop()
k, n = map(int,input().split())

s = list()
data = list(i for i in range(k + 1))

result = 0
back()

print(result%int(1e9))
'''

# dp 문제, 표를 통해 결과 도출을 해야한다.
n, k = map(int,input().split())
dp = [[0] * (k + 1) for _ in range(n + 1)]

dp[0][0] = 1
for i in range(n + 1):
  for j in range(1, k + 1):
    dp[i][j] = dp[i-1][j] + dp[i][j-1]
# n이 1일때... n이 n-1일때
# k가 1일때... 
print(dp[n][k] % 1000000000)
