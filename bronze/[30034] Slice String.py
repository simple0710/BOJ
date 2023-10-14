# 2023/09/16 Implementation, String, DataStructures
# https://www.acmicpc.net/problem/30034
import sys
input = sys.stdin.readline

def solution():
  # 문자 구분자
  # 문자열을 구분자로 나눈다.
  M = int(input())
  string_split = input().rstrip().split()

  # 숫자 구분자
  # 문자열을 구분자로 나눈다
  K = int(input())
  number_split = input().rstrip().split()
  total_split = set(string_split + number_split)

  # 병합자
  # 문자열을 합치는 조건(구분자를 상쇄하는 개념)
  K = int(input())
  k = input().rstrip().split()
  for i in k:
    total_split.discard(i)

  # 문자열
  S = int(input())
  string = input().rstrip()

  # 병합자가 아닌 구분자로 문자열을 나눈다.
  for i in total_split:
    if i in total_split:
      string = ' '.join(string.split(i))

  # 나누어진 문자열 출력
  for i in string.split():
    print(i)

# 기준 문자열
if __name__ == "__main__":
  solution()