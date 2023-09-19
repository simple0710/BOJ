# 2023/08/12 Implementation, Sorting
# https://www.acmicpc.net/problem/28455
N = int(input())
level = 0
state = 0
char = []
for i in range(N):
  v = int(input())
  char.append(v)
char.sort(reverse=True) # 내림차순 정렬
for i in char[:42] if N >= 42 else char:
  level += i
  for j in [60, 100, 140, 200, 250]: # 능력치 상승 기준
    if i >= j: # 능력치 상승 기준을 넘긴 경우
      state += 1 # 스탯 증가
# 레벨의 합, 상승한 능력치의 합 출력
print(level, state)