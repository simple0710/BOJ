# 2023/09/12 Math, Geometry, PolygonArea
# https://www.acmicpc.net/problem/2166
import sys
input = sys.stdin.readline

def solution(N, point):
  x, y = 0, 0
  for i in range(N):
    # x좌표를 다음 y좌표에 곱한 총 합을 구한다.
    # y좌표를 다음 x자표에 곱한 총 합을 구한다.
    x += point[i-1][0] * point[i][1]
    y += point[i-1][1] * point[i][0]
  # 두번째 결과를 첫번째 결과에 뺀다.
  return round(abs(x - y) / 2, 1)

def main():
  N = int(input())
  point = []
  for _ in range(N):
    a, b = map(int,input().split())
    point.append((a, b))
  print(solution(N, point)) # 정답 출력

if __name__ == "__main__":
  main()