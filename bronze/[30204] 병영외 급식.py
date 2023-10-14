# 2023/10/07 Math, Ad-Hoc
# https://www.acmicpc.net/problem/30204
N, X = map(int,input().split())
data = list(map(int,input().split()))
if sum(data) % X == 0: # 모든 사람의 수 % X인 경우 급식 가능
  print(1)
else: # 불가능
  print(0)