# 2023/05/20 DP
# https://www.acmicpc.net/problem/22114
import sys
input = sys.stdin.readline

def solution():
  dp = [[0] * (N) for _ in range(2)]
  # data는 N - 2까지 탐색
  # dp는 N - 1까지 탐색
  for i in range(1, N):
    now = data[i - 1]
    # 다음 칸의 거리가 K보다 같거나 작은 경우
    # 이전 칸 + 1을 한다.
    if now <= K:
      dp[0][i] = dp[0][i-1] + 1
      dp[1][i] = dp[1][i-1] + 1
    # 다음 칸의 거리가 K보다 큰 경우
    # 거리 제한이 없이 블럭을 점프한다.
    else:
      dp[1][i] = dp[0][i-1] + 1
  # 정답 비교 후, 큰 값 출력
  print(max(max(dp[0]), max(dp[1])) + 1)

N, K = map(int,input().split())
data = list(map(int,input().split()))
# 탐색 시작
solution()