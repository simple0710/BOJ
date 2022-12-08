# 2022/11/29 그리디 알고리즘
# https://www.acmicpc.net/problem/11501
import sys
input = sys.stdin.readline

for _ in range(int(input())):
  N = int(input())
  data = list(map(int,input().split()))
  check = 0
  res = 0
  # 맨 뒤에서 부터 확인한다.
  for i in range(N-1, -1, -1):
    # 해당 값이 자신보다 크다면 교체
    if check <= data[i]:
      check = data[i]
    # 자신보다 작다면 판매
    else:
      res += check - data[i]
  # 정답 출력
  print(res)