# 2023/09/02 Implementation, Sorting
# https://www.acmicpc.net/problem/2535
from collections import defaultdict
import sys
input = sys.stdin.readline

def solution():
  students.sort(key=lambda x : -x[2]) # 점수 정렬
  nation = defaultdict(int)
  cnt = 0
  for n, sn, score in students:
    if nation[n] < 2: # 수상 국가가 2명 미만인 경우
      cnt += 1
      print(n, sn)
      if cnt == 3: # 금, 은, 동을 모두 수상한 경우 종료
        break
      nation[n] += 1

if __name__ == "__main__":
  N = int(input())
  students = [list(map(int,input().split())) for _ in range(N)]
  solution() # 탐색 시작