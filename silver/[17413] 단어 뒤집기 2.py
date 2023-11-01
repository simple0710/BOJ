# 2023/06/17 Implementation, DataStructures, String
# https://www.acmicpc.net/problem/17413
string = input()
flag = False
check = []
for i in string:
  if i == '<' or i == ' ':
    if i == '<': # 태그가 시작하는 경우
      flag = True
    # check에는 공백이 포함되지 않으므로 end=' '
    print(''.join(map(str, check[::-1])), end='' if flag else ' ')
    check.clear()
  if flag: # 태그 안에 존재하는 경우
    print(i, end='')
    if i == '>': # 태그가 닫히는 경우
      flag = False
  else: # 태그 바깥인 경우
    if i != ' ': # 공백을 제외한 문자열을 추가한다.
      check.append(i)
else:
  # check가 남은 경우 출력
  print(''.join(map(str, check[::-1])))