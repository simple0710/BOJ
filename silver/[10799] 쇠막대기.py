# 2023/07/03 DataStructure, Stack
# https://www.acmicpc.net/problem/10799
data = input().replace('()', '*')
res = 0
cnt = 0
for i in data:
  if i == '(': # 막대기의 시작인 경우
    cnt += 1
  elif i == ')': # 막대기의 끝인 경우
    res += 1
    cnt -= 1
  else: # 레이저인 경우
    res += cnt
# 정답 출력
print(res)