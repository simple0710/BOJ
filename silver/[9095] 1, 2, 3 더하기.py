# 2022/11/12 다이나믹 프로그래밍
def sol(n):
  if n == 1:
    return 1
  elif n == 2:
    return 2
  elif n == 3:
    return 4
  else:
    return sol(n-1) + sol(n-2) + sol(n-3)

# 4 이상의 n에 대한 값은 이전 3개의 경우의 수의 합과 같다. 
for _ in range(int(input())):
  n = int(input())
  print(sol(n))