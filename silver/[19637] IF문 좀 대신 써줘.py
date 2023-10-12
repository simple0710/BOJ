# 2023/10/12 BinarySearch
# https://www.acmicpc.net/problem/19637
import sys
input = sys.stdin.readline

def binary_search(N, now_power, data):
  s = 0
  e = N-1
  while s <= e:
    mid = (s + e) // 2
    if now_power > int(data[mid][1]): # 현재 전투력이 해당 상한값보다 큰 경우
      s = mid + 1
    else: # 현재 전투력이 상한값 이하인 경우 칭호 저장
      res = mid
      e = mid - 1
  return data[res][0] # 칭호 반환

def solution(N, M, data, power):
  # 정답 출력
  for now_power in power:
    print(binary_search(N, now_power, data))

def main():
  N, M = map(int,input().split())
  # 칭호와 전투력 상한값 N개를 입력 받는다.
  data = [list(input().rstrip().split()) for _ in range(N)]
  # 구해야 하는 전투력을 M개 입력 받는다.
  power = [int(input()) for _ in range(M)]
  solution(N, M, data, power) # 코드 실행

if __name__ == "__main__":
  main()