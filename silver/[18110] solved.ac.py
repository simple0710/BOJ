# 2023/08/16 Math, Implementation, Sorting
# https://www.acmicpc.net/problem/18110
import sys
input = sys.stdin.readline

def round_(v):
  # 파이썬의 round는 오사오입으로 
  # 5 미만의 숫자는 내림, 5 초과의 숫자는 올림이다.
  # 만약 반올림할 자릿수가 5일 경우 5의 앞자리가 홀수인 경우 올림, 짝수인 경우 내린다.
  if v - int(v) >= 0.5:
    return int(v) + 1
  else:
    return int(v)

def solution(n, data):
  if n == 0: # 값이 없는 경우
    return 0
  d = round_(n * 0.15) # 절사평균을 이용한 제외할 사람값 구하기
  if n > 1: # 제외할 사람이 한 명이상인 경우
    return round_(sum(data[d : -d]) / (n - 2 * d))
  else: # 제외할 사람이 없는 경우
    return round_(sum(data) / n)
  
def main():
  N = int(input())
  data = [int(input()) for _ in range(N)]
  data.sort() # 배열 정렬
  print(solution(N, data))

if __name__ == "__main__":
  main()