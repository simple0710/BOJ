# 2023/09/29 DP
# https://www.acmicpc.net/problem/4883
import sys
input = sys.stdin.readline
MAX = sys.maxsize

def solution():
  dp = [[[] for _ in range(3)] for _ in range(N)]
  # 가장 위쪽 가운데 정점에서 시작했을 때 최솟값을 저장해 둔다.
  dp[1][0] = graph[1][0] + graph[0][1]
  dp[1][1] = graph[1][1] + min(dp[1][0], graph[0][1], graph[0][1] + graph[0][2])
  dp[1][2] = graph[1][2] + min(dp[1][1], graph[0][1], graph[0][1] + graph[0][2])
  for i in range(2, N):
    for j in range(3):
      dp[i][j] = graph[i][j] + min(dp[i][j-1] if j >= 1 else MAX, dp[i-1][j-1] if j >= 1 else MAX, dp[i-1][j], dp[i-1][j+1] if j < 2 else MAX)
  return dp[N-1][1] # 가장 아래쪽 가운데 정점의 비용 최솟값 반환

def main():
  global N, graph
  t = 1
  while True:
    N = int(input())
    if N == 0: # 종료
      break
    graph = [list(map(int,input().split())) for _ in range(N)]
    print(f'{t}. {solution()}') # 테스트 케이스, 비용 출력
    t += 1

if __name__ == "__main__":
  main()