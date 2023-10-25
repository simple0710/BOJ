# 2023/09/08 Implementation, Sorting
# https://www.acmicpc.net/problem/29791
import sys
input = sys.stdin.readline

def solution():
  recent1 = 0
  recent2 = 0
  res1 = 0
  res2 = 0
  if total[0][1] == 0: # 에르다 노바인 경우
    res1 += 1
    recent1 = total[0][0]
  else: # 오리진 스킬인 경우
    res2 += 1
    recent2 = total[0][0]
  t = total[0][0] # 맨 처음의 경우
  for i in range(1, N+M):
    if total[i][1] == 0: # 에르다 노바인 경우
      # 에르다 노바를 처음 사용한 경우와의 차이가 100이상인 경우
      # 아직 스킬을 사용하지 않은 경우
      if total[i][0] - recent1 >= 100 or recent1 == 0:
        recent1 = total[i][0] # 최근 값 갱신
        # 행동 불가 조건
        # 면역 시간
        if t + 90 < total[i][0] or res1 == 0:
          t = total[i][0]
          res1 += 1
    elif total[i][1] == 1: # 오리진 스킬인 경우
      # 절대 행동 불가 증가 조건
      # 오리진 스킬을 처음 사용한 경우와의 차이가 360이상인 경우
      # 아직 스킬을 사용하지 않은 경우
      if total[i][0] - recent2 >= 360 or recent2 == 0:
        recent2 = total[i][0]
        res2 += 1
  # 몬스터 행동 불가, 절대 행동 불가 상태 출력
  print(res1, res2)

if __name__ == "__main__":
  # 에르다 노바 사용 횟수, 오리진 스킬 사용 횟수
  N, M = map(int,input().split())
  total = []
  # 에르다 노바의 단축키를 누른 시점
  for i in list(map(int,input().split())):
    total.append((i, 0))
  # 오리진 스킬의 단축키를 누른 시점
  for i in list(map(int,input().split())):
    total.append((i, 1))
  total.sort() # 시점 순으로 정렬
  solution()