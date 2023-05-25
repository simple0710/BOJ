# 2023/05/25 Math, DP, BruteForce
# https://www.acmicpc.net/problem/2502
D, K = map(int,input().split())
dp = [0] * (D + 1)
dp[1] = 1
dp[2] = 1
for i in range(3, D + 1): # 증가 값
  dp[i] = dp[i-1] + dp[i-2]

# 1일과 2일이 증가하면 각 자리의 값이 2배
# 2일이 증가하면 각 자리의 값 전의 값만큼 증가
for i in range(1, K // dp[-1] + 1):
  check = (K - dp[-1] * i) % dp[-2]
  if not check: # K와 같은 값이 되는 경우
    f = i
    s = i + (K - dp[-1] * i) // dp[-2]
    break

# 정답 출력
print(f)
print(s)