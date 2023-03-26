# 2023/03/24 Implementation
# https://www.acmicpc.net/problem/10102
N = int(input())
data = input()
a = data.count('A')
b = data.count('B')

# 각 조건에 맞는 정답 출력
if a > b:
  print('A')
elif a < b:
  print('B')
else:
  print('Tie')