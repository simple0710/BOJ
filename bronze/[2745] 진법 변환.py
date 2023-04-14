# 2023/04/14 Math, String, Implementation
# https://www.acmicpc.net/problem/2745
N, B = input().split()
B = int(B)
res = 0
for idx, i in enumerate(N[::-1]):
  if i.isalpha(): # 알파벳인 경우
    res += (ord(i) - ord('A') + 10) * B**idx
  else: # 숫자인 경우
    res += int(i) * B**idx
# 정답 출력
print(res)