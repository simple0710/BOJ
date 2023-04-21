# 2023/04/16 Math
# https://www.acmicpc.net/problem/27959
N, M = map(int,input().split())
if N * 100 >= M: # 가지고 있는 돈이 더 많은 경우
  print("Yes")
else: # 가격이 더 큰 경우
  print("No")