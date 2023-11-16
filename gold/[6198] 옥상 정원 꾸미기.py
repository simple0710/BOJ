# 2023/11/16 DataStructures, Stack
# https://www.acmicpc.net/problem/6198
import sys
input = sys.stdin.readline

def solution(N, building_list):
  stack = []
  res = 0
  for height in building_list:
    # 현재 건물의 높이보다 최근 건물의 높이가 더 낮은 경우 제거
    while stack and stack[-1] <= height:
      stack.pop()
    stack.append(height) # 현재 위치 추가
    res += len(stack) - 1 # 확인할 수 있는 수 갱신
  return res # 벤치마킹이 가능한 빌딩의 수의 합 반환

def main():
  # 빌딩의 개수
  N = int(input())
  # 빌딩의 높이
  building_list = [int(input()) for _ in range(N)]
  # 벤치마킹이 가능한 빌딩의 수의 합 출력
  print(solution(N, building_list))

if __name__ == "__main__":
  main()