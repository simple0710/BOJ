# 2023/09/10 Implementation, Simulation
# https://www.acmicpc.net/problem/29729
import sys
input = sys.stdin.readline

def solution(res):
  cnt = 0
  for _ in range(N+M):
    a = int(input())
    if a == 0: # 배열의 끝에서 원소를 삭제하는 명령
      cnt -= 1
      if cnt < 0:
        cnt = 0
    else: # 배열에 원소를 저장하는 명령
      cnt += 1
      if cnt > res: # 배열의 크기를 벗어난 경우
        # 배열 크기 2배 증가
        res *= 2
  return res # 가변 배열의 최대 크기 반환

if __name__ == "__main__":
  S, N, M = map(int,input().split())
  print(solution(S)) # 가변 배열의 최대 크기 출력