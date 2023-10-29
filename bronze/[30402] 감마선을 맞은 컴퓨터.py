# 2023/10/28 Implementation, String
# https://www.acmicpc.net/problem/30402
import sys
input = sys.stdin.readline

def main():
  white = False
  black = False
  gray = False
  for _ in range(15):
    pixel = input().rstrip().split()
    if 'w' in pixel: # 춘배 사진을 발견한 경우
      white = True
    elif 'b' in pixel: # 나비 사진을 발견한 경우
      black = True
    elif 'g' in pixel: # 영철 사진을 발견한 경우
      gray = True
  # 발견한 고양이 사진에 따른 정답 출력
  if gray:
    print("yeongcheol")
  elif white:
    print("chunbae")
  elif black:
    print("nabi")

if __name__ == "__main__":
  main()