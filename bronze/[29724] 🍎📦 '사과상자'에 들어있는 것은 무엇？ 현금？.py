# 2023/09/10 Math
# https://www.acmicpc.net/problem/29724
import sys
input = sys.stdin.readline

def solution():
  res1 = 0
  res2 = 0
  for _ in range(N):
    # T, W, H, L
    # 상자의 종류, 가로, 높이, 세로
    data = input().split()
    a, b, c = map(int, data[1:]) # 상자 종류 제외
    if data[0] == 'A': # 종류가 A인 경우
      a //= 12 # 가로에 놓을 수 있는 사과의 수
      b //= 12 # 높이에 높을 수 있는 사과의 수
      c //= 12 # 세로에 놓을 수 있는 사과의 수
      # 상자 질량 = 1000 + 총 사과 개수 * 500
      res1 += 1000 + a * b * c * 500
      # 값어치 = 총 사과 개수 * 4000
      res2 += a * b * c * 4000
    elif data[0] == 'B': # 종류가 B인 경우
      res1 += 6000
  # 상자의 질량, 시장 사과 가격 출력
  print(res1, res2)

if __name__ == "__main__":
  N = int(input())
  solution() # 코드 실행