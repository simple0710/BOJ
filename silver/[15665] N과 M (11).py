# 2023/01/09 백트래킹
# https://www.acmicpc.net/problem/15665
def dfs(s):
  if len(s) == M:
    word = ''.join(map(str, s))
    if word in res:
      return
    res.add(word)
    print(*s)
    return
  for i in range(N):
    s.append(arr[i])
    dfs(s)
    s.pop()

if __name__=="__main__":
  N, M = map(int,input().split())
  arr = sorted(list(map(int,input().split())))
  res = set()
  dfs([])
