# 2023/06/11 Combinatorics, BFS, BruteForce, Math
# https://www.acmicpc.net/problem/17471
from collections import deque, defaultdict
import sys, itertools
input = sys.stdin.readline

def bfs(same):
  now = same[0]
  q = deque([now])
  visited = set([now])
  check = 0
  while q:
    v = q.popleft()
    check += population[v]
    for ar in area[v]: # 인접 구역 확인
      if ar not in visited and ar in same: # 방문학 적이 없고, same에 존재하는 경우
        q.append(ar)
        visited.add(ar)
  # 인구수의 합, 방문 길이 반환
  return check, len(visited)

N = int(input())
population = [int(x) for x in input().split()]
area = defaultdict(list)
for i in range(N): # 인접 구역 데이터 저장
  data = list(map(int,input().split()))
  for j in range(1, data[0] + 1):
    area[i].append(data[j] - 1)

res = sys.maxsize
# 탐색 시작
for i in range(1, N // 2 + 1): # 절반의 경우만 구해도 된다.
  combis = list(itertools.combinations(range(N), i)) # 가능한 조합 구하기
  for comb in combis:
    s1, v1 = bfs(comb) # 조합 1
    s2, v2 = bfs([i for i in range(N) if i not in comb]) # 조합 2 (나머지)
    if v1 + v2 == N: # 두 방문 기록이 N과 같은 경우 작은 값으로 정답 갱신
      res = min(res, abs(s1 - s2))

if res == sys.maxsize: # 정답이 변하지 않은 경우 -1출력
  print(-1)
else: # 그렇지 않은 경우 res 출력
  print(res)