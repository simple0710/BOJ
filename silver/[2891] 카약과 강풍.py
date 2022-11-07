# 2022/11/07 그리디 알고리즘
import sys
input = sys.stdin.readline

# 정보 입력
N, S, R = map(int,input().split())
BreakTeam = list(map(int,input().split()))
MoreTeam = list(map(int,input().split()))
BreakTeam.sort()
MoreTeam.sort()

# 카약 추가분을 가지고 있는 팀에 대해서 while 수행
while MoreTeam:
  x = MoreTeam.pop(0)
  if x in BreakTeam:
    BreakTeam.remove(x)
  elif x-1 in BreakTeam:
    BreakTeam.remove(x-1)
  elif x+1 in BreakTeam:
    BreakTeam.remove(x+1)

# 정답 출력
print(len(BreakTeam))