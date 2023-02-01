# 2023/01/30 재귀
# https://www.acmicpc.net/problem/12919
import sys
input = sys.stdin.readline

def dfs(s):
  if len(s) == len(S):
    if s == S: # S와 같은 경우 1을 출력 후 종료
      print(1)
      sys.exit(0)
    return
  # 마지막이 A인 경우
  if s[-1] == 'A':
    dfs(s[:-1])
  # 시작이 B인 경우
  if s[0] == 'B':
    dfs(s[::-1][:-1])

S = input().rstrip()
T = input().rstrip()

# 탐색 시작
dfs(T)

# 불가능
print(0)