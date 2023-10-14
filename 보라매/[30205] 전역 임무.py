# 2023/10/07 Greedy, Sorting
# https://www.acmicpc.net/problem/30205
import sys
input = sys.stdin.readline

# 기지 수 N, 기지의 층수 M, 김 병장의 전투력 P
N, M, P = map(int,input().split())
# 기지의 정보(층수는 마음대로 조작)
data = [sorted(list(map(int,input().split()))) for _ in range(N)]
res = 1
for i in range(N):
  cnt = 0
  for j in data[i]:
    if j == -1: # 아이템인 경우
      cnt += 1
    else:
      if j <= P: # 적군의 전투력이 김 병장의 전투력보다 낮은 경우
        P += j # 김 병장의 전투력이 적군의 전투력만큼 증가
      else: # 적군의 전투력이 긴 병장의 전투력보다 큰 경우
        flag = False
        while cnt: # 아이템을 가지고 있는 경우
          cnt -= 1
          P *= 2 # 전투력 2배 증가
          if j <= P: # 다시 확인
            P += j
            flag = True
            break
        if not flag: # 아이템을 써도 이기지 못한 경우
          print(0) # 0출력 후 종료
          sys.exit(0)
  while cnt: # 남은 아이템으로 전투력 증가
    cnt -= 1
    P *= 2
print(1) # 가능