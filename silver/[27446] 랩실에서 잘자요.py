# 2023/02/13 그리디
# https://www.acmicpc.net/problem/27446
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
arr = sorted(list(set(map(int,input().split()))))
search = []
for i in range(1, N + 1): # 없는 페이지의 정보를 얻는다.
  if i not in arr:
    search.append(i)

K = 1
res = 0
if search:
  s = search.pop(0)
  while search:
    x = search.pop(0)
    if abs(x-s) <= 3: # 4개 이상 뽑는 경우 손해
      K += abs(x-s)
    else:
      res += 5 + 2 * K
      K = 1
    s = x
  res += 5 + 2 * K
# 정답 출력
print(res)