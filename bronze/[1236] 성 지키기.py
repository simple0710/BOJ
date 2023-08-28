# 2023/08/20 Implementation
# https://www.acmicpc.net/problem/1236
import sys
input = sys.stdin.readline

def solution(N, M, data):
  check1 = 0
  check2 = 0
  # X가 없는 행의 값을 구한다.
  for i in range(N):
    if 'X' not in data[i]:
      check1 += 1
  # X가 없는 열의 값을 구한다.
  for j in range(M):
    if 'X' not in [data[i][j] for i in range(N)]:
      check2 += 1
  # 가장 큰 값을 반환한다.
  return max(check1, check2)

def main():
  N, M = map(int,input().split())
  data = [input().rstrip() for _ in range(N)]
  # 탐색 및 정답 출력
  print(solution(N, M, data))

if __name__ == "__main__":
  main()