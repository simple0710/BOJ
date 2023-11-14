# 2023/08/22 Bruteforcing, PigeonholePrinciple
# https://www.acmicpc.net/problem/20529
import sys
input = sys.stdin.readline

def solution(N, data):
  # MBTI는 총 16개에 각각 두 개씩 있다면 32이다.
  # 따라서 32를 초과하면 정답은 0이 된다.
  if N > 32:
    return 0
  res = 100
  for i in range(N-2): # 모든 경우를 탐색해 본다.
    for j in range(i+1, N):
      for k in range(j+1, N):
        check = 0
        for n in range(4):
          if data[i][n] != data[j][n]: # A, B
            check += 1
          if data[i][n] != data[k][n]: # A, C
            check += 1
          if data[j][n] != data[k][n]: # B, C
            check += 1
        res = min(res, check) # 최저값 갱신
  return res # 정답 반환

def main():
  # 학생의 수
  N = int(input())
  # 각 학생의 MBTI 성격 유형
  data = list(map(str, input().rstrip().split()))
  print(solution(N, data)) # 탐색 및 정답 출력

if __name__ == "__main__":
  T = int(input())
  for _ in range(T):
    main()