# 2023/08/06 MST
# https://www.acmicpc.net/problem/4386
import math

def find(x): # 부모 루트 찾기
  if parent[x] != x:
    parent[x] = find(parent[x])
  return parent[x]

def union(a, b): # 부모 루트 합치기
  a = find(a)
  b = find(b)
  parent[max(a, b)] = min(a, b)

N = int(input())

star = []
distance_data = []
for i in range(N):
  x, y = map(float, input().split())
  star.append((x, y))
  for j in range(i):
    # 거리, 연결 된 별
    distance_data.append((float(f'{math.sqrt(abs(star[j][0] - x) ** 2 + abs(star[j][1] - y) ** 2) : .2f}'), i, j))

distance_data.sort()

parent = [i for i in range(N)]

res = 0
for c, x, y in distance_data:
  if find(x) != find(y): # 부모 루트가 같지 않은 경우
    union(x, y)
    res += c

print(res) # 정답 출력