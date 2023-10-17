# 2023/08/04 MST
# https://www.acmicpc.net/problem/1922
def find(x): # 부모 루트를 찾는다.
  if parent[x] != x:
    parent[x] = find(parent[x])
  return parent[x]

def union(a, b): # 부모 루트를 동일하게 한다.
  a = find(a)
  b = find(b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

N = int(input())
M = int(input())

parent = [i for i in range(N + 1)]

computer = []
for _ in range(M):
  a, b, c = map(int,input().split())
  computer.append((c, a, b))

computer.sort() # 비용 순으로 정렬

res = 0
for c, a, b in computer:
  if find(a) != find(b): # 부모가 다른 경우
    union(a, b)
    res += c
print(res) # 정답 출력