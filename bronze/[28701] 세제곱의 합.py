# 2023/08/13 Math, Implementation
# https://www.acmicpc.net/problem/28701
N = int(input())
res = 0
res1 = 0
for i in range(1, N + 1):
   res += i
   res1 += i**3
print(res) # 1부터 N까지 수의 합
print(res ** 2) # 1부터 N까지 수의 합을 제곱한 수
print(res1) # 1부터 N까지 수의 세제곱의 합