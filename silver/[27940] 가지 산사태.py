# 2023/04/08 Greedy, Ad-Hoc
# https://www.acmicpc.net/problem/27940
import sys
input = sys.stdin.readline

N, M, K = map(int,input().split())
res = -1
check = 0 # 빗물의 합
for ind in range(M):
  t, r = map(int, input().split())
  check += r
  if check > K and res == -1: # 빗물의 양이 K를 넘은 경우 res 저장
    res = (ind+1, 1)
# 정답 출력
if res == -1:
  print(-1)
else:
  print(' '.join(map(str, res)))