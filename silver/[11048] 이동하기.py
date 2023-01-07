# 2022/12/28 DP
# https://www.acmicpc.net/problem/11048
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
maze = [list(map(int,input().split())) for _ in range(N)]
dp = [[0] * M for _ in range(N)]
dp[0] = maze[0]
# 맨 처음 가로
for i in range(1, M):
  dp[0][i] = dp[0][i-1] + maze[0][i]

for i in range(1, N):
  for j in range(M):
    # 맨 처음 세로
    if j == 0:
      dp[i][j] = dp[i-1][j] + maze[i][j]
      continue
    # 그 외 해당 구역에 올 수 있는 루트의 최대값과 현재 위치의 값을 더한다.
    dp[i][j] = max(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + maze[i][j]

# 정답 출력
print(dp[N-1][M-1])

# 같지만 다른 풀이
# dp 배열을 하나씩 더 늘려서 계산한다.
import sys
input = sys.stdin.readline
N, M = map(int,input().split())
dp = [[0] * (M+1) for _ in range(N+1)]
maze = [list(map(int,input().split())) for _ in range(N)]
for i in range(1, N+1):
  for j in range(1, M+1):
    dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + maze[i-1][j-1]
print(dp[N][M])