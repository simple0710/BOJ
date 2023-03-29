# 2023/03/29 Prefix Sum
# https://www.acmicpc.net/problem/2015
from collections import defaultdict
import sys
input = sys.stdin.readline

N, K  = map(int,input().split())
data = list(map(int,input().split()))

for i in range(1, N): # 누적합 구하기
  data[i] += data[i-1]

res = 0
pre = defaultdict(int)
for i in range(N):
  if data[i] == K: # 누적합이 K인 경우
    res += 1
  res += pre[data[i]-K]
  pre[data[i]] += 1
print(pre)
# 정답 출력
print(res)