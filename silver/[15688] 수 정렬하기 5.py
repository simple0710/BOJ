# 2023/11/26 Sorting
# https://www.acmicpc.net/problem/15688
import sys
input = sys.stdin.readline

def main():
  N = int(input())
  data = [int(input()) for _ in range(N)]
  data.sort() # 오름차순 정렬
  # 정답 출력
  for i in data: print(i)

if __name__ == "__main__":
  main()