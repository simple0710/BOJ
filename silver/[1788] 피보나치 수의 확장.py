# 2023/09/18 Math, DP
# https://www.acmicpc.net/problem/1788
import sys
input = sys.stdin.readline

def solution1(N):
  if N == 0:
    print(0)
    print(0)
  else:
    dp = [0] * (abs(N)+1)
    dp[0:1] = [0, 1]
    if N > 0: # 양수인 경우
      # 0, 1, 1, 2, ...
      for i in range(2, abs(N)+1):
        dp[i] = (dp[i-2] + dp[i-1]) % 1000000000
    else: # 음수인 경우
      # 1, 0, 1, -1, ...
      for i in range(2, abs(N)+1):
        dp[i] = dp[i-2] - dp[i-1]
        if dp[i] < 0:
          dp[i] = (abs(dp[i]) % 1000000000) * -1
        else:
          dp[i] = dp[i] % 1000000000

    # 정답 출력(F(n)이 양수인지 음수 여부, F(n))
    if dp[abs(N)] > 0:
      print(1)
    else:
      print(-1)
    print(abs(dp[abs(N)]))

def solution2(N):
  if N == 0: # 0인 경우
    print(0)
    print(0)
  else: # 0이 아닌 경우
    dp = [0] * (abs(N)+1)
    dp[0:1] = [0, 1]
    for i in range(2, abs(N)+1):
      dp[i] = (dp[i-2] + dp[i-1]) % 1000000000
    # N이 양수이거나, N % 2가 0이 아닌 경우 양수
    if N > 0 or abs(N) % 2 != 0:
      print(1)
    else: # 그 외의 경우 음수
      print(-1)
    print(dp[abs(N)]) # F(n) 출력

def main():
  N = int(input())
  solution1(N)

if __name__ == '__main__':
  main()