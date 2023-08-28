# 2023/08/16 Math, Implementation
# https://www.acmicpc.net/problem/27865
import sys
input = sys.stdin.readline
flush = sys.stdout.flush

N = int(input())
cnt = 1
while cnt <= N:
  print(f'? {cnt}') # 물어보기
  flush()
  res = input().rstrip() # 가지고 있는지 입력
  flush()
  if res == 'Y': # 가지고 있으면 해당 수 출력
    print(f'! {cnt}')
    flush()
    break