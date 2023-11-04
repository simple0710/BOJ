# 2023/11/04 Implementation, String, Bruteforcing, Backtracking
# https://www.acmicpc.net/problem/7490
import sys
input = sys.stdin.readline

def back(depth, total, s, num):
  if depth == N+1: # 모든 기호 삽입 완료
    # 합이 0인 경우 정답 출력
    # 계산하지 못한 num을 더한다.
    if total + num == 0:
      print(s)
    return
  # 숫자를 붙인다.
  back(depth+1, total, s+f' {depth}', int(str(num)+str(depth)))
  # 이어 붙이기를 그만 두고, 더하기, 빼기를 한다.
  back(depth+1, total+num, s+f'+{depth}', depth)
  back(depth+1, total+num, s+f'-{depth}', -depth)

def solution():
  # 1을 들고 2부터 시작한디.
  back(2, 0, '1', 1) 

def main():
  global N
  T = int(input()) # 테스트 케이스 수
  for _ in range(T):
    N = int(input()) # 자연수
    solution() # 코드 실행
    print()

if __name__ == "__main__":
  main()