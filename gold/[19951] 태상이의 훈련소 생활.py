# 2023/03/27 Prefix Sum
# https://www.acmicpc.net/problem/19951
N, M = map(int,input().split())
data = list(map(int,input().split()))
check = [0] * (N + 1)
# 시작 부분과 마지막 부분 값 변경 
for _ in range(M):
  a, b, k = map(int,input().split())
  check[a-1] += k
  check[b] -= k

dp = [0] * (N + 1)
dp[0] = check[0]
for i in range(1, N+1): # 누적 합 구하기
  dp[i] = dp[i-1] + check[i]

# 정답 출력
for i in range(N):
  print(data[i] + dp[i], end=' ')