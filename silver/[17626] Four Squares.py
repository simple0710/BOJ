# 2023/08/21 DP, Bruteforcing
# https://www.acmicpc.net/problem/17626
import sys
input = sys.stdin.readline

def solution(N):
  dp = [0, 1]
  for i in range(2, N + 1):
    v = int(1e9)
    j = 1
    while j ** 2 <= i:
      v = min(v, dp[i-(j**2)])
      j += 1
    dp.append(v + 1)
  return dp[N] # 정답 반환

def main():
  N = int(input())
  print(solution(N)) # 탐색 및 정답 출력

if __name__ == "__main__":
  main()