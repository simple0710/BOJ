# 2023/10/10 Implementation
# https://www.acmicpc.net/problem/1205
import sys
input = sys.stdin.readline

def solution(ranking, N, S, P):
  r = N + 1 # 최대 등수
  idx = 1
  for i in ranking[:P]:
    if S > i: # 새 점수가 더 큰 경우
      return min(r, idx)
    elif S == i: # 점수가 같은 경우 가장 작은 등수 저장
      r = min(r, idx)
    else: # 새 점수가 더 낮은 경우
      idx += 1
  if N < P: # 모든 랭킹 P를 채우지 못한 경우
    return r
  return -1 # 랭킹에 등재될 수 없는 경우

def main():
  N, S, P = map(int,input().split())
  if N > 0: # 점수가 존재하는 경우
    ranking = sorted(list(map(int,input().split())), reverse=True)
    print(solution(ranking, N, S, P)) # 등수 출력
  else: # 아무 점수도 없는 경우
    print(1)

if __name__ == "__main__":
  main()