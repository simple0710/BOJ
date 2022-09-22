# 백트래킹
def dfs():
  if len(s) == m:
    print(' '.join(map(str,s)))
    return
  # 트리 구조를 생각한다.
  ## 1(pop) - (2,3,4) 각각 pop()
  ## 2(pop) - (1,2,3) 각각 pop()
  for i in range(1, n+1):
    if i not in s:
      s.append(i)
      dfs()
      s.pop()  
n, m = map(int, input().split())
s = list()
dfs()