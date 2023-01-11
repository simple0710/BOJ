# 2023/01/10 백트래킹
# https://www.acmicpc.net/problem/15666
import sys
input = sys.stdin.readline

def dfs(stx, s):
  if len(s) == M:
    # 완성된 내용 res에 저장 후 출력
    word = ' '.join(map(str, s))
    if word not in res:
      res.add(word)
      print(*s)
    return
  for i in range(stx, N):
    s.append(arr[i])
    dfs(i, s)
    s.pop()

if __name__=="__main__":
  N, M = map(int,input().split())
  arr = sorted(list(map(int, input().split())))
  res = set()
  # 탐색 시작 및 정답 출력
  dfs(0, [])