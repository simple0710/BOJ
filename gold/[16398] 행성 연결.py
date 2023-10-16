# 2023/08/05 MST
# https://www.acmicpc.net/problem/16398
def find(x): # 부모 루트 탐색
  if parent[x] != x:
    parent[x] = find(parent[x])
  return parent[x]

def union(a, b): # 부모 루트 통일
  a = find(a)
  b = find(b)
  parent[max(a, b)] = min(a, b)

N = int(input())
planet = []
for i in range(N):
  cost = list(map(int,input().split()))
  for j in range(N):
    if i != j:
      planet.append((cost[j], i, j))

planet.sort() # 비용순으로 정렬

parent = [i for i in range(N)]

res = 0
for cost, a, b in planet:
  if find(a) != find(b): # 부모가 같지 않은 경우
    union(a, b)
    res += cost

print(res) # 정답 출력