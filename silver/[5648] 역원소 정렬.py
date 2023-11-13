# 2023/11/13 Sorting
# https://www.acmicpc.net/problem/5648
import sys
input = sys.stdin.readline

def main():
  # 원소 개수, 원소값
  length, *numbers = input().split()
  # 원소 채우기
  while len(numbers) < int(length):
    numbers.extend(input().split())
  # 원소를 거꾸로 뒤집고 오름차 순으로 정렬한 값을 출력
  print(*sorted([int(i[::-1]) for i in numbers]), sep='\n')

if __name__ == "__main__":
  main()