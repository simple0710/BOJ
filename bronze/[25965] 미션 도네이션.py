# 2023/09/03 Math, Implementation
# https://www.acmicpc.net/problem/25965
import sys
input = sys.stdin.readline

if __name__ == "__main__":
  N = int(input())
  for _ in range(N):
    M = int(input())
    mission = [list(map(int,input().split())) for _ in range(M)]
    k, d, a = map(int,input().split())
    res = 0
    for k_, d_, a_ in mission: # 미션 확인
      total = k * k_ + a * a_ - d * d_
      if total > 0: # 합계가 0보다 큰 경우 더한다
        res += total
    print(res) # 정답 출력