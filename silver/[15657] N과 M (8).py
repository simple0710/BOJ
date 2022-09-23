# 백트래킹
def dfs(start):
  if len(s) == m:
    print(' '.join(map(str,s)))
    return
  for i in range(start, len(data)):
    s.append(data[i])
    dfs(i)
    s.pop()    
n, m = map(int,input().split())
data = list(map(int,input().split()))
data.sort()
s = []
dfs(0)