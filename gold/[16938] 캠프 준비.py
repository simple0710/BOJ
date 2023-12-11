# 2023/12/11 Bruteforcing, Backtracking
# https://www.acmicpc.net/problem/16938
def solution(depth):
  global res
  if depth == N: # 모든 문제를 확인한 경우 문제들을 확인한다.
    if len(s) >= 2: # 두 문제 이상인 경우를 확인한다.
      total_score = sum(s) # 총 합
      score_diffrence = max(s) - min(s) # 가장 어려운 난이도 - 가장 쉬운 난이도
      # 기준을 충족하면 방법의 수에 추가한다.
      if L <= total_score <= R and X <= score_diffrence: res += 1
    return
  s.append(difficult[depth])
  # 현재 문제를 추가한 경우
  solution(depth+1)
  s.pop()
  # 현재 문제를 추가하지 않은 경우
  solution(depth+1)

def main():
  global N, L, R, X, difficult, res, s
  N, L, R, X = map(int,input().split())
  difficult = list(map(int,input().split()))
  s = []
  res = 0
  solution(0) # 탐색 시작
  print(res) # 방법의 수 출력

if __name__ == "__main__":
  main()