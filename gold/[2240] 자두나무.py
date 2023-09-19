# 2023/09/19 DP
# https://www.acmicpc.net/problem/2240
import sys
input = sys.stdin.readline
# 왼쪽에 있는 경우, 오른쪽에 있는 경우, 왼쪽->오른쪽, 오른쪽->왼쪽
# 이동한 경우 최댓값
# w의 제한을 어떻게 해결할 것인가?

def solution(T, W, falling):
  # 위치 1과 위치 2로 나눈다.
  dp = [[[0] * 2 for _ in range(W+1)] for _ in range(T+1)]
  for i in range(T+1):
    for j in range(W+1):
      # 위치 1(떨어지는 위치)
      # 원래 자리를 유지하거나, 위치를 이동한 경우를 비교한다.
      # 이때, -1번 위치를 변경한 경우를 확인하지 않도록 해야 한다.
      dp[i][j][falling[i]] = max(dp[i-1][j][falling[i]], 0 if j == 0 else dp[i-1][j-1][(falling[i]+1) % 2]) + 1

      # 위치 2 (떨어지는 위치 반대)
      dp[i][j][(falling[i]+1) % 2] = dp[i-1][j][(falling[i]+1) % 2]
  # 모든 경우 확인
  res = max([max(i) for i in dp[-1]]) - 1 # 쓰레기 값 제거
  return res # 자두의 최대 개수 반환

def main():
  T, W = map(int,input().split())
  falling = [0] + [int(input()) - 1 for _ in range(T)]
  print(solution(T, W, falling)) # 정답 출력

if __name__ == "__main__":
  main()