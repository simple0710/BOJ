# 2023/01/09 백트래킹
# https://www.acmicpc.net/problem/15664
def dfs(st, s):
  if len(s) == M:
    word = ' '.join(map(str, s))
    # 만약 있는 경우 return
    if word in res:
      return
    res.add(word)
    print(*s)
    return
  for i in range(st, N):
    s.append(arr[i])
    dfs(i+1, s)
    s.pop()
    
if __name__=="__main__":
  N, M = map(int,input().split())
  arr = sorted(list(map(int,input().split())))
  res = set()
  dfs(0, [])
