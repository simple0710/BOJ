# 2023/11/03 DataStructures, Stack
# https://www.acmicpc.net/problem/1863
import sys
input = sys.stdin.readline

def solution(apart_height):
  stack = []
  res = 0
  for y in apart_height:
    # 마지막으로 확인한 값이 현재 높이보다 큰 경우 건물 수 증가
    # ex) 1 3, 2 2
    while stack and stack[-1] > y:
      res += 1
      stack.pop()
    if stack and stack[-1] == y: # 같은 값은 넘긴다.
      continue
    stack.append(y) # 현재 높이 추가
  while stack: # 남은 층수가 있는 경우
    # 마지막 높이가 0보다 크다면 건물 수 증가
    if stack[-1] > 0: res += 1
    stack.pop()
  # 최소 건물 개수 출력
  return res 
  
def main():
  # 스카이 라인 고도 수
  N = int(input())
  # 스카이 라인 고도가 바뀌는 지점(지점, 높이)
  data = [list(map(int,input().split()))[1] for _ in range(N)]
  # 최소 건물 개수 출력
  print(solution(data))

if __name__ == "__main__":
  main()