# 2023/08/12 Implementation
# https://www.acmicpc.net/problem/28453
N = int(input())
for i in list(map(int,input().split())):
  if i == 300: # 구간 1
    check = 1
  elif i >= 275: # 구간 2
    check = 2
  elif i >= 250: # 구간 3
    check = 3
  else: # 구간 4
    check = 4
  print(check, end = ' ') # 구간 출력