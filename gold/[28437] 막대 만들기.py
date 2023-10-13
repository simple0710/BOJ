# 2023/08/08 Math, DP, NumberTheory
# https://www.acmicpc.net/problem/28437
import sys
input = sys.stdin.readline

N = map(int,input().split())
stick_type = list(map(int,input().split()))
Q = int(input())
q_data = list(map(int,input().split()))
MAX = 100000

dp = [0] * (MAX + 1)
for i in stick_type:
  dp[i] = 1

for x in range(2, MAX + 1):
  for k in range(1, int(x ** (1/2)) + 1):
    # ex) x = 6, k = 2일 때, 3으로도 2를 만들 수 있고, 2로도 3을 만들 수 있다.
    if x % k == 0: # k로 나누어 지는 경우 x를 만들 수 있다.
      dp[x] += dp[k]
      # 1. k * k != x : 위의 조건에 이미 더했으므로 같은 경우는 더하지 않는다.
      # 2. k != 1 : 1이 있으면 x // k와 k는 같은 값이므로 더하지 않는다.
      if k * k != x and k != 1: # 반대의 경우
        dp[x] += dp[x//k]

for i in q_data: # 정답 출력
  print(dp[i], end = ' ')