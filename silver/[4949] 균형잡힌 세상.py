# 2023/08/16 DataStructures, String, Stack
# https://www.acmicpc.net/problem/4949
while True:
  s = input()
  if s == '.': # 마지막 입력
    break
  check = []
  for i in s:
    if i == '(' or i == '[': # 여는 괄호 데이터 추가
      check.append(i)
    elif i == ')': # 닫는 소괄호인 경우
      if check and check[-1] == '(': # 여는 소괄호가 짝을 이루면 제거
        check.pop()
      else: # 없으면 불가능
        print('no')
        break
    elif i == ']':
      if check and check[-1] == '[': # 여는 대괄호가 짝을 이루면 제거
        check.pop()
      else: # 없으면 불가능
        print('no')
        break
  else:
    if check: # 모든 괄호가 짝을 이루지 못한 경우 no 출력
      print('no')
    else: # 모든 괄호가 짝을 이룬 경우 yes 출력
      print('yes')