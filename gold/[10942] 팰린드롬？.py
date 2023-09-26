# 2023/09/26 DP
# https://www.acmicpc.net/problem/10942
import sys
input = sys.stdin.readline

def dp_get(N, number):
  dp = [[0] * N for _ in range(N)]
  # 순서는 해당 수의 길이 i를 가지고 끝까지 탐색한다.
  # 즉, 행은 시작 지점, 열은 끝 지점이 된다.
  for i in range(N): # 수의 길이
    for s in range(N-i): # 시작 지점
      e = s + i # 끝 지점
      # 길이가 1인 경우
      # 양 끝이 같고, 길이가 2인 경우
      # 양 끝이 같고, s+1, e-1 -> 양 쪽으로 한 칸씩 작은 구역이 펠린드롬인 경우
      if s == e or (number[s] == number[e] and (dp[s+1][e-1] or s+1 == e)):
        dp[s][e] = 1
  return dp # dp 결과 반환

def main():
  N = int(input())
  number = list(map(str,input().split()))
  dp = dp_get(N, number)
  M = int(input())
  for _ in range(M): # 질문 시작
    s, e = map(int,input().split())
    print(dp[s-1][e-1]) # 정답 출력

if __name__ == "__main__":
  main()