# 2023/11/06 Bruteforcing
# https://www.acmicpc.net/problem/14658
import sys
input = sys.stdin.readline

def solution():
  max_ = 0
  # 가로 길이가 가장 작고, 세로 길이가 가장 작은 값을 모두 고려한다.
  # 가로 좌표, 세로 좌표를 따로 구성해 구역을 탐색한다.
  for x1, y1 in star:
    for x2, y2 in star:
      cnt = 0
      for vx, vy in star:
        # x1, y2 지점에서 그린 사각형 안에 포함되는 경우 cnt + 1
        if x1 <= vx <= x1 + L and y2 <= vy <= y2 + L:
          cnt += 1
      max_ = max(max_, cnt) # 최댓값 갱신
  return K - max_ # 지구에 부딪히는 별똥별 반환

def main():
  global N, M, L, K, star
  # 가로 길이, 세로 길이, 트램펄린 한 변의 길이, 별똥별의 수
  N, M, L, K = map(int,input().split())
  # 별똥별이 떨어지는 위치
  star = [list(map(int,input().split())) for _ in range(K)]
  print(solution()) # 지구에 부딪히는 별똥별의 개수 출력

if __name__ == "__main__":
  main()