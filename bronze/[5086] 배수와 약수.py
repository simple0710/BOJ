# 2023/03/08 구현
# https://www.acmicpc.net/problem/5086
while True:
  a, b = map(int,input().split())
  if a + b == 0: # 둘 다 0인 경우 종료
    break
  elif b % a == 0: # a가 b의 약수인 경우
    print("factor")
  elif a % b == 0: # a가 b의 배수인 경우
    print("multiple")
  else: # 둘 다 아닌 경우
    print("neither")