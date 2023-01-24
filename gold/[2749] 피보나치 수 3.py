# 2023/01/21 Math
# https://www.acmicpc.net/problem/2749
N = int(input())

# 주기의 길이가 P일 때, N % mod == N % P % mod
# M = 10**k 일 때, 주기는 항상 15*10**(k-1)
# ex) M = 3, P = 8, N = 8, fn = 21, N % 8 = 0, 0번째 피보나치 수는 0
# 이 문제에서 M = 10**6 이기 때문에 주기는 15 * 10**5
mod = 1000000
dp = [0, 1]
p = mod // 10 * 15
for i in range(2, p):
  dp.append((dp[i-2] + dp[i-1]) % mod)

# 정답 출력
print(dp[N%p])