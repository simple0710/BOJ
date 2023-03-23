# 2023/03/23 Greedy
# https://www.acmicpc.net/problem/1679
import sys
input = sys.stdin.readline

N = int(input())
use_number = list(map(int,input().split()))
max_cnt = int(input())

s = 1
t = 1
while True:
  p = 0
  check = s
  for i in use_number[::-1]: # 큰 수부터 계산해본다.
    p += check // i
    check %= i
  if p > max_cnt: # 사용한 수의 개수를 초과한 경우 종료
    if t == 1: # 홀순이 차례에서 진 경우
      name = 'jjaksoon'
    else: # 짝순이 차례에서 진 경우
      name = "holsoon"
    # 정답 출력
    print(f"{name} win at {s}")
    break
  s += 1
  t = (t + 1) % 2