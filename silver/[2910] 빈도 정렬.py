# 2023/11/14 DataStructures, Sorting, Hash-Set
# https://www.acmicpc.net/problem/2910
from collections import defaultdict
import sys
input = sys.stdin.readline

def solution(N, data):
  count = defaultdict(int)
  # 개수 파악
  for i in data: count[i] += 1
  # 빈도 내림차순 정렬
  res = sorted(count.items(), key=lambda x: -x[1])
  # 정답 출력
  for key, cnt in res:
    print(str(key) + (' ' + str(key)) * (cnt-1), end = ' ')

def main():
  # 수열의 개수, 숫자 크기 제한
  N, C = map(int,input().split())
  # 메시지의 수열
  data = list(map(int,input().split()))
  solution(N, data) # 코드 실행

if __name__ == "__main__":
  main()