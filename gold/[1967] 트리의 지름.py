# 2023/08/01 Trees, DFS
# https://www.acmicpc.net/problem/1967
# 부모에서 현재 가지고 있는 가중치를 들고 자식을 탐색한다
# 비교할 것 : 끝까지 탐색 후 현재 가지고 있는 가중치 vs 한 부모가 가진 가중치의 합
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def dfs(parent):
  global res
  check = [0]
  for child, weight in tree[parent]:
    f = dfs(child)
    check.append(weight + f)
  # 현재 값과 지금까지의 가중치 값으로 만든 직선을 비교한다.
  # 이진 트리가 아니기 때문에 2개의 자식 노드 중 가장 큰 2개의 노드로 비교한다.
  res = max(res, sum(sorted(check)[-2:]))
  return max(check) # 가장 긴 가중치의 합 반환
  
N = int(input())
tree = [[] for _ in range(N + 1)]
for _ in range(N-1):
  p, c, w = map(int,input().split())
  tree[p].append((c, w))
res = 0
# 탐색 시작
dfs(1)

# 정답 출력
print(res)