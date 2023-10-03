# 2023/10/03 DP
# https://www.acmicpc.net/problem/2482
import sys
input = sys.stdin.readline

def solution(N, K):
  dp = [[0] * (K+1) for _ in range(N+1)]
  for i in range(N+1):
    # i개의 색 중에 0개를 선택하는 경우 : 1
    dp[i][0] = 1
    # i개의 색 중에 1개를 선택하는 경우 : i
    dp[i][1] = i
    if i >= 2:
      for j in range(2, K+1):
        if i == N: # 원형이므로 처음 색과 닿는 위치
          # 주변 색을 포함시키지 않고 j개의 색을 선택하는 경우의 수
          # i번째 색을 포함시키지 않고 j개의 색을 선택하는 경우의 수
          dp[i][j] = dp[i-3][j-1] + dp[i-1][j]
        else:
          # i번째 색을 포함시키고, i-1을 제외한 j개의 색을 선택하는 경우의 수
          # i번째 색을 포함시키지 않고 j개의 색을 선택하는 경우의 수
          dp[i][j] = dp[i-2][j-1] + dp[i-1][j]
        dp[i][j] %= int(1e9)+3
  return dp[N][K] # N가지 색을 인접하지 않도록 K개의 색을 선택하는 경우의 수 반환

def main():
  N = int(input())
  K = int(input())
  print(solution(N, K)) # 정답 출력

if __name__ == "__main__":
  main()