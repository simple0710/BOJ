# 백트래킹
def dfs(start):
  if len(s) == m:
    print(' '.join(map(str,s)))
    return
  # start를 추가함으로써 앞의 숫자가 뒤의 숫자보다 작은 경우를 제외한다.
  for i in range(start, n+1):
    # i가 s에 있지 않은 경우
    if i not in s:
      # 추가
      s.append(i)
      # 시작 지점을 한 칸 옮긴다.
      dfs(i+1)
      # pop()
      s.pop()
n, m = map(int, input().split())
s = list()
dfs(1)