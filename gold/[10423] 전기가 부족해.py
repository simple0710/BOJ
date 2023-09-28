# 2023/08/06 MST, KruskalAlgorithm
# https://www.acmicpc.net/problem/10423
# 풀이 1 : 발전소에 대한 조건을 이용하여 문제 해결
# 풀이 2 : 발전소를 0으로 처리한 다음 탐색
def find(x): # 부모 루트 찾기
  if parent[x] != x:
    parent[x] = find(parent[x])
  return parent[x]

def union(a, b): # 부모 루트 합치기
  a = find(a)
  b = find(b)
  parent[max(a, b)] = min(a, b)
  # if a in power_plant: # a가 발전소에 연결되어 있으면 b의 부모를 a로 한다
  #   parent[b] = a
  # else: # a의 부모를 b로 한다
  #   parent[a] = b

N, M, K = map(int,input().split())
power_plant = list(map(int,input().split()))

cable = []
for _ in range(M):
  u, v, w = map(int,input().split())
  cable.append((w, u, v))

cable.sort()
parent = [i if i not in power_plant else 0 for i in range(N + 1)]
res = 0
for w, u, v in cable:
  check_u = find(u)
  check_v = find(v)
  # 조건 1 : 둘 다 발전기면 안된다.
  # 조건 2 : 이미 연결되어 있다면, 다른 발전기에 연결되면 안된다.
  # if ((u in power_plant) & (v in power_plant)): # 조건 1
  #   continue
  # if ((check_u in power_plant) & (check_v in power_plant)): # 조건 2
  #   continue
  if check_u != check_v: # 부모가 다른 경우
    union(u, v)
    res += w

# 정답 출력
print(res)