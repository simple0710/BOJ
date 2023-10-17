# 2023/08/03 MST
# https://www.acmicpc.net/problem/1647
def find(x): # 현재 노드 확인
  if p[x] != x:
    p[x] = find(p[x])
  return p[x]

def union(a, b): # 부모 노드 합치기
  a = find(a)
  b = find(b)
  if a < b:
    p[b] = a
  else:
    p[a] = b

N, M = map(int,input().split())
graph = []
for _ in range(M):
  a, b, c = map(int,input().split())
  graph.append([c, a, b])

graph.sort() # 가중치를 오름차 순으로 정렬
    
p = [0] * (N + 1)
for i in range(1, N + 1):
  p[i] = i

s = []
res = 0
for c, a, b in graph:
  if find(a) != find(b): # 같은 부모를 가지고 있는지 확인
    union(a, b) # 부모 노드를 합친다
    res += c
    s.append(c)
res -= s.pop() # 두 마을이기 때문에 길 하나를 삭제한다

# 정답 출력
print(res)