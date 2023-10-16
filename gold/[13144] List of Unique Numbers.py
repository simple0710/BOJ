# 2023/09/04 TwoPointer
# https://www.acmicpc.net/problem/13144
import sys
input = sys.stdin.readline

def solution():
  check = [False] * 100001
  cnt = 0
  s = 0
  e = 0
  while e < N:
    if check[arr[e]]: # 중복되는 숫자가 있는 경우
      if check[arr[s]] == check[arr[e]]: # 현재 위치와 같은 숫자인 경우
        check[arr[s]] = False # 중복에서 제거
      s += 1
    else: # 중복되는 숫자가 없는 경우
      check[arr[e]] = True
      e += 1
      cnt += e - s # 횟수 추가
  return cnt

if __name__ == "__main__":
  N = int(input())
  arr = list(map(int,input().split()))
  print(solution()) # 정답 출력