def back_tracking(start):
  # 해당 길이일 경우
  if len(s) == L:
    check_m = 0
    for z in ['a', 'e', 'i', 'o', 'u']:
      if z in s: # 만약 모음이 들어갈 경우 check_m += 1을 수행한다.
        check_m += 1
    # 자음의 개수는 총 길이세서 모음의 길이를 뺀 값
    check_j = L - check_m
    # 자음이 2개 이상, 모음이 1개 이상일 경우 출력
    if check_j >= 2 and check_m >= 1:
      print(''.join(map(str, s)))
    return
  for i in range(start, len(data)):
    # data[i]가 없는 경우 추가하고 재귀를 수행, pop()을 수행하고 다음으로 넘어간다.
    if data[i] not in s:
      s.append(data[i])
      back_tracking(i + 1)
      s.pop()
# 문자열의 길이, 문자의 개수를 입력 받는다.
L, C = map(int, input().split())
data = list(map(str,input().split()))
data.sort()
s = list()
back_tracking(0)
