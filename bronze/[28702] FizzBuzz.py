# 2023/08/13 Math, String
# https://www.acmicpc.net/problem/28702
res = 0
index = 0
for i in range(3):
  string = input()
  if string.isdigit(): # 숫자인 경우
    check = int(string)
    index = i

# 마지막으로 나온 숫자에 따른 숫자 추측
if index == 2:
  res = check + 1
elif index == 1:
  res = check + 2
else:
  res = check + 3

# 3의 배수, 5의 배수 확인 후 정답 출력
if res % 3 == 0 and res % 5 == 0:
  print("FizzBuzz")
elif res % 3 == 0:
  print("Fizz")
elif res % 5 == 0:
  print("Buzz")
else:
  print(res)