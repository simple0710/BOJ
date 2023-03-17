# 2023/03/17 Implementation
# https://www.acmicpc.net/problem/10886
a, b = 0, 0
for _ in range(int(input())):
  if int(input()): # 투표에 따른 값 추가
    a += 1
  else:
    b += 1
# 정답 출력
print("Junhee is ", end='')
if a < b:
  print("not cute!")
else:
  print("cute!")