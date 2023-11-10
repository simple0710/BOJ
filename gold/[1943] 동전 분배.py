# 2023/11/10 DP, Knapsack
# https://www.acmicpc.net/problem/1943
import sys
input = sys.stdin.readline

def solution(N, data, total):
  half_total = total // 2
  dp = [True] + [False] * half_total
  for unit, cnt in data:
    for m in range(half_total, unit-1, -1):
      if dp[m-unit]: # 현재 금액에서 단위를 뺀 경우가 True인 경우
        for j in range(cnt): # 있는 개수만큼 확인
          if m + unit * j <= half_total: # 더한 합이 절반 이하인 경우
            dp[m + unit * j] = True # 가능
          else: # 종료
            break
  return 1 if dp[-1] else 0 # 나누어 줄 수 있는지 여부 반환

def main():
  for _ in range(3):
    # 동전의 종류
    N = int(input())
    total = 0
    data = []
    for _ in range(N):
      # 단위, 개수
      unit, cnt = map(int,input().split())
      data.append((unit, cnt))
      total += unit * cnt
    # 나눌 수 있는지를 출력
    print(solution(N, data, total) if total % 2 == 0 else 0)

if __name__ == "__main__":
  main()