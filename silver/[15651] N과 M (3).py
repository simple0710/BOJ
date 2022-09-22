# 백트래킹
def dfs():
  if len(s) == m:
    print(' '.join(map(str, s)))
    return
  for i in range(1, n+1):
    # if i not in s 가 없어 중복을 허용한다.
    s.append(i)
    dfs()
    s.pop()

n, m = map(int, input().split())
s = []
dfs()