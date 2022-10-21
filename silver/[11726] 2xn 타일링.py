def solution(n):
  if n == 1:
    return 1
  
  dp = [0] * (n + 1)
  dp[1] = 1
  dp[2] = 2
  # 증가 수치는 피보나치 수열과 동일하다
  for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 10007
  return dp[n]

n = int(input())
print(solution(n))