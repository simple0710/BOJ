# 2023/07/15 Ad-Hoc
# https://www.acmicpc.net/problem/28292
N = int(input())
if N >= 6: # 3이 최대
  N = 3
elif N >= 3: # 2가 최대
  N = 2
else: # 1이 최대
  N = 1
# 정답 출력
print(N)