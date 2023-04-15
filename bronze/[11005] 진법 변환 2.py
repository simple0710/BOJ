# 2023/04/15 Math, Implementation
# https://www.acmicpc.net/problem/11005
N, B = map(int, input().split())
number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

res = ''
# 진법 변환
while N != 0:
  res += str(number[N % B])
  N //= B

# 정답 출력
print(res[::-1])