# 2022/10/26
# 크루스칼 알고리즘
# 유니온 파인드
# 크루스칼 알고리즘 진행 방식
# 1. root 저장 배열 생성
# 2. 간선들을 가중치 기준으로 정렬
# 3. 간선들이 이은 두 정점을 find함수를 통해 두 root(find(s), find(e))를 찾는다.
# 4. 두 root가 다르다면 큰 root 값을 작은 root값으로 만들어 연결되게 해준다.
# 5. 가중치를 더한다.
import sys
input = sys.stdin.readline

def union(a, b):
  a = find(a)
  b = find(b)
  if b < a:
    parent[a] = b
  else:
    parent[b] = a

def find(a):
  if a == parent[a]:
    return a
  parent[a] = find(parent[a])
  return parent[a]

v, e = map(int,input().split())
edge = []
for _ in range(e):
  a, b, w = map(int,input().split())
  edge.append((w, a, b))

edge.sort(key=lambda x: x[0]) # 간선들의 가중치를 오름차 순으로 정렬
parent = list(range(v + 1))

sum = 0
for w, s, e in edge:
  if find(s) != find(e):
    union(s, e)
    sum += w

print(sum)