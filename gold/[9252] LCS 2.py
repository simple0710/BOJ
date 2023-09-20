# 2023/09/20 DP
# https://www.acmicpc.net/problem/9252
import sys
input = sys.stdin.readline

def solution(s1, s2):
  dp = [[""] * len(s2) for _ in range(len(s1))]
  for i in range(1, len(s1)):
    for j in range(1, len(s2)):
      if s1[i] == s2[j]: # 같은 문자인 경우
        # 이전 경우의 가장 긴 문자열을 더한다.
        dp[i][j] = dp[i-1][j-1] + s1[i]
      else: # 다른 문자인 경우
        # 이전 경우 중 가장 긴 문자열을 가져온다.
        dp[i][j] = dp[i-1][j] if len(dp[i-1][j]) >= len(dp[i][j-1]) else dp[i][j-1]
  res = dp[-1][-1]
  # 길이, 문자열 출력
  return len(res), res

def main():
  string1 = " " + input().rstrip()
  string2 = " " + input().rstrip()
  # 정답 출력
  print(*solution(string1, string2), sep='\n')

if __name__ == "__main__":
  main()