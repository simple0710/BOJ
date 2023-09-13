# 2023/06/17 Implemnetation, Bruteforce, Combinatiorics
# https://www.acmicpc.net/problem/28238
from itertools import combinations
import sys
input = sys.stdin.readline

N = int(input())
# 요일 5개중 2개를 중복없이 선택한다.
combi = list(combinations(range(5), 2))
check = [0] * len(combi)
for i in range(N):
  v = list(map(int,input().split()))
  for index, com in enumerate(combi):
    x, y = com
    if v[x] and v[y]: # 학생의 요일별 참가 가능 여부와 비교
      check[index] += 1
res = [0] * 5
# 최대 인원 및 조합 중 가장 많이 참여할 수 있는 답을 저장한다.
max_people = max(check)
res_check = combi[check.index(max_people)]
res[res_check[0]] = 1
res[res_check[1]] = 1
# 최대 인원과, 특강 일정을 출력한다.
print(max_people)
print(' '.join(map(str, res)))