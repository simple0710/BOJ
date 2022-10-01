def back_tracking(start):
  # 길이가 6이면 출력
  if len(s) == 6:
    print(' '.join(map(str,s)))
    return
  # 수를 추가하고 다음 수를 받는다.
  for i in range(start, len(data)):
    s.append(data[i])
    back_tracking(i+1)
    s.pop()

while True:
  # 맨 처음 값은 번호의 수
  data = list(map(int,input().split()))
  if data[0] == 0:
    break
  data = data[1:]
  data.sort()
  s = list()
  back_tracking(0)
  print()
