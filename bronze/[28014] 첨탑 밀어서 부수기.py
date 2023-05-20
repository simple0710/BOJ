# 2023/05/06 Greedy
# https://www.acmicpc.net/problem/28014
N = int(input())
s = 0
res = 0
for i in list(map(int,input().split())):
  if s <= i:
    res += 1
  s = i
# 정답 출력
print(res)