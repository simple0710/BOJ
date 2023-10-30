# 2023/06/28 Implementation, Greedy
# https://www.acmicpc.net/problem/2891
N, S, R = map(int,input().split())
s_team = list(map(int,input().split()))
r_team = list(map(int,input().split()))
# 여분의 카약이 있는 팀은 자신의 것을 사용
cnt = 0
sf_team = []
for i in s_team:
  if i not in r_team:
    sf_team.append(i)
  else:
    cnt += 1
    r_team.remove(i)
# 카약 빌리기
for i in sf_team:
  if i-1 in r_team:
    cnt += 1
    r_team.remove(i-1)
    continue
  if i+1 in r_team:
    cnt += 1
    r_team.remove(i+1)
# 정답 출력
print(S - cnt)