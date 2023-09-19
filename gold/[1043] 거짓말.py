# 2023/08/02 DataStructures, Disjoin-Set
# https://www.acmicpc.net/problem/1043
# 목표 : 진실을 아는 사람이 몇명인지 구한다.
N, M = map(int,input().split())
know_p_data = list(map(int, input().split()))
know_p = set(know_p_data[1:])
party_list = []
for _ in range(M):
  party_list.append(list(map(int,input().split()))[1:])

visited = [False] * (N + 1)
res = M
if know_p_data[0] > 0: # 진실을 아는 사람이 있는 경우
  while know_p:
    check = know_p.pop()
    for i in range(M):
      if check in party_list[i]: # 현재 파티 확인
        for j in party_list[i]:
          if not visited[j]: # 진실을 모르는 사람 추가
            know_p.add(j)
            visited[j] = True
  for i in party_list: # 진실을 아는 사람이 있는 파티 탐색
    for j in i:
      if visited[j]:
        res -= 1
        break
# 정답 출력
print(res)