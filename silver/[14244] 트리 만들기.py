# 2023/05/02 Tree
# https://www.acmicpc.net/problem/14244
N, M = map(int,input().split())
leaf = 0
last_leaf = 0
for i in range(1, N):
  if M > leaf: # leaf보다 M이 더 큰 경우
    print(0, i)
    leaf += 1
  else: # 그렇지 않은 경우
    print(last_leaf, i)
  last_leaf = i