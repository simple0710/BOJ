# 2023/08/09 MST, Kruskal
# https://www.acmicpc.net/problem/13418
# 내리막이 다시 오르막이 된다 해도 최초 조사 기준
# 출발은 입구(0)에서 시작
# 오르막의 수가 k일 때, k ** 2 피로도 증가
import sys
input = sys.stdin.readline

def find(x, p): # 부모 찾기
  if p[x] != x:
    p[x] = find(p[x], p)
  return p[x]

def union(a, b, p): # 부모 합치기
  a = find(a, p)
  b = find(b, p)
  p[max(a, b)] = min(a, b)

def question(a, b, c, p): # 길 찾기
  check = 0
  if find(a, p) != find(b, p):
    union(a, b, p)
    if c == 0: # 오르막인 경우
      check = 1
  return check

N, M = map(int,input().split())

road = []
for _ in range(M + 1):
  A, B, C = map(int,input().split())
  road.append((C, A, B))

road.sort(reverse=True)

best_parent = [i for i in range(N + 1)]
worst_parent = [i for i in range(N + 1)]
best_res = 0
worst_res = 0
for i in range(M + 1):
  # a, b 비교 
  now = road[i]
  best_res += question(now[1], now[2], now[0], best_parent)
  worst_now = road[-i - 1]
  worst_res += question(worst_now[1], worst_now[2], worst_now[0], worst_parent)

print(worst_res**2 - best_res**2) # 최악 - 최적 정답 출력