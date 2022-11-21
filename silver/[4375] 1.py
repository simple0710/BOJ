# 2022/11/21 수학
while True:
  # 값이 없는 경우는 종료
  try:
    n = int(input())
  except:
    break
  num = 0
  i = 1
  while True:
    # 1111...으로 진행
    num = num * 10 + 1
    # 만약 n으로 나누어지면 정답 출력
    if num % n == 0:
      print(i)
      break
    i += 1