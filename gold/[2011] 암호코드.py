# 2023/10/02 DP
# https://www.acmicpc.net/problem/2011
import sys
input = sys.stdin.readline

def solution(password):
  dp = [0] * len(password)
  dp[0] = 1
  for i in range(1, len(password)):
    if password[i] > '0': # 한자리 패스워드가 가능한 경우
      dp[i] += dp[i-1]
    if 10 <= int(password[i-1:i+1]) <= 26: # 2자리가 가능한 경우
      dp[i] += dp[i-2]
  return dp[-1] % 1000000 # 정답 출력

def main():
  password = ' ' + input().rstrip()
  print(solution(password)) # 정답 출력

if __name__ == "__main__":
  main()