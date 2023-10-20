# 2023/10/20 Math
# https://www.acmicpc.net/problem/23971
import sys, math
input = sys.stdin.readline

def get(a, b):
  return math.ceil(a/(b+1))

def solution(W, H, N, M):
  # H행 / 가로 간격
  # W열 / 세로 간격
  return get(H, M) * get(W, N) # 최대 수용 가능 인원 반환

def main():
  W, H, N, M = map(int,input().split())
  print(solution(W, H, N, M)) # 최대 수용 가능 인원 출력

if __name__ == "__main__":
  main()