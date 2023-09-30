# 2023/09/30 DP
# https://www.acmicpc.net/problem/2670
import sys
input = sys.stdin.readline

def solution(N, data):
  dp = [[] for _ in range(N)]
  dp[0] = data[0]
  for i in range(1, N):
    dp[i] = max(data[i], dp[i-1] * data[i]) # 현재 값과 이전 값 * 현재 값의 값 비교
  return '%0.3f' % max(dp) # 정답 반환

def main():
  N = int(input())
  data = [float(input()) for _ in range(N)]
  print(solution(N, data)) # 정답 출력

if __name__ == "__main__":
  main()