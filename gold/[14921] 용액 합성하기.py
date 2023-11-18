# 2023/11/18 TwoPointer
# https://www.acmicpc.net/problem/14921
import sys
input = sys.stdin.readline

def solution(N, data):
  # 양 끝에서 시작
  s = 0
  e = N-1
  min_value = data[s] + data[e]
  while s < e:
    value = data[s] + data[e]
    if abs(min_value) > abs(value): # 최솟값 갱신
      min_value = value
    # 합이 음수면 s 증가
    if value < 0: s += 1
    # 합이 양수면 e 감소
    else: e -= 1
  return min_value # 0에 가장 가까운 특성값 반환

def main():
  # 용액의 개수
  N = int(input())
  # 오름차 정렬된 용액 정보
  data = list(map(int,input().split()))
  print(solution(N, data)) # 0에 가장 가까운 특성값 출력

if __name__ == "__main__":
  main()