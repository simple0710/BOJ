# 2023/08/20 Implementation, String
# https://www.acmicpc.net/problem/1235
import sys
input = sys.stdin.readline

def solution(N, data):
  for i in range(1, len(data[0]) + 1):
    check = set()
    for j in range(N):
      check.add(data[j][:i])
    if len(check) == N: # 서로 다른 번호가 N과 같은 경우
      return i

def main():
  N = int(input())
  data = [input().rstrip()[::-1] for _ in range(N)]
  print(solution(N, data)) # 탐색 및 정답 출력

if __name__ == "__main__":
  main()