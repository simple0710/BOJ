import sys
input = sys.stdin.readline

def dfs(v):
  if visited[v] == False:
    visited[v] = True

    for i in data[v]:
      # data[2]에 3 있으면 tmp_up.add(2), tmp_bottom.add(3)
      tmp_up.add(v) # 넣은 값. main, 
      tmp_bottom.add(i) # 넣어져 있는 값
      # 위와 아래가 같으면 set 자체에 추가
      if tmp_up == tmp_bottom:
        ans.extend(list(tmp_bottom))
        return
      dfs(i)

n = int(input())
data = [[] for _ in range(n+1)]

for i in range(1, n + 1):
  v = int(input())
  data[i].append(v)

ans = []

for i in range(1, n + 1):
  visited = [False] * (n + 1)
  tmp_up = set()
  tmp_bottom = set()
  dfs(i)

ans = list(set(ans))
ans.sort()

# 길이와 원소 출력
print(len(ans))
for i in ans:
  print(i)