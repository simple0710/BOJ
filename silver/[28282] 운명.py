# 2023/08/11 Math
# https://www.acmicpc.net/problem/28282
from collections import defaultdict
import sys
input = sys.stdin.readline

X, K = map(int,input().split())
data = list(map(int,input().split()))

# 1. 딕셔너리(O(N**2))
left = defaultdict(int)
right = defaultdict(int)
for i in range(X):
  left[data[i]] += 1
  right[data[X+i]] += 1

res = 0
for i in left.keys():
  for j in right.keys():
    if i != j:
      res += left[i] * right[j]

print(res) # 정답 출력

# 2. 수학(O(N))
colors = [0] * (K + 1)
left = data[:X]
right = data[X:]

for i in right:
  colors[i] += 1

res = 0
for i in left:
  res += X - colors[i] # 총 양말의 수 - 현재 색깔의 양말의 수

print(res) # 정답 출력