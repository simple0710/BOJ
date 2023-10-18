# 2023/08/04 MST
# https://www.acmicpc.net/problem/6497
def find(x): # 부모 노드 찾기
  if parent[x] != x:
    parent[x] = find(parent[x])
  return parent[x]

def union(a, b): # 부모 노드 합치기
  a = find(a)
  b = find(b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

while True:
  M, N = map(int,input().split())
  if M + N == 0: # 입력이 0 0인 경우 종료
    break
  house = []
  for i in range(N):
    x, y, z = map(int,input().split())
    house.append((z, x, y))

  house.sort() # 비용순으로 정렬

  parent = [i for i in range(M)]
  res = 0
  for z, x, y in house:
    if find(x) != find(y): # 부모 노드가 같지 않은 경우
      union(x, y)
    else: # 길 제거
      res += z
  # 정답 출력
  print(res)