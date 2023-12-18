# 2023/12/18 Math, DP, Combinatorics
# https://www.acmicpc.net/problem/10422
def get_dp():
  dp = [0] * 5001
  dp[0] = 1
  for i in range(2, 5001, 2):
    for j in range(2, i+2, 2):
      # 왼쪽 괄호의 경우의 수 * 오른쪽 괄호의 경우의 수
      dp[i] += dp[j-2] * dp[i-j]
    dp[i] %= 1000000007
  return dp # 계산한 결과 반환

def main():
  T = int(input())
  dp = get_dp() # 올바른 문자열 개수를 담은 dp 저장
  for _ in range(T):
    L = int(input())
    print(dp[L]) # 올바른 문자열 개수 출력

if __name__ == "__main__":
  main()