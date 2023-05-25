# 2023/05/24 Math, Greedy
# https://www.acmicpc.net/problem/28062
N = int(input())
data = sorted(list(map(int,input().split())))
a = []
b = []
for i in data:
  if i % 2 == 0: # 짝수
    a.append(i)
  else: # 홀수
    b.append(i)
res = sum(a) + sum(b)
# 정답 출력
if len(b) % 2: # 홀수의 개수가 홀수인 경우 합이 홀수가 된다.
  print(res - b[0])
else:
  print(res)