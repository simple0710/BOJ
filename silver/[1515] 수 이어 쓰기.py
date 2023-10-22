# 2023/10/22 Implementation, String, Greedy, Bruteforcing
# https://www.acmicpc.net/problem/1515
import sys
input = sys.stdin.readline

def solution(data):
  s = 0 # 찾고자 하는 수
  while True:
    s += 1
    ns = str(s)
    while len(ns) and len(data):
      if ns[0] == data[0]: # 같은 값이 나온 경우
        # 해당 값을 제외
        data = data[1:]
      ns = ns[1:] # 찾고자 하는 문자열 줄이기
    if not data: # 남은 수가 없는 경우 정답 반환
      return s

def main():
  data = input().rstrip()
  print(solution(data)) # 정답 출력

if __name__ == "__main__":
  main()