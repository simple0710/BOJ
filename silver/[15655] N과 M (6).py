# 백트래킹
def dfs(start):
  if len(s) == m:
    print(' '.join(map(str, s)))
    return
  for i in range(start, len(data)):
    if data[i] not in s:
      s.append(data[i])
      dfs(i + 1)
      s.pop()
n, m = map(int,input().split())
data = list(map(int,input().split()))
s = list()
data.sort()
dfs(0)