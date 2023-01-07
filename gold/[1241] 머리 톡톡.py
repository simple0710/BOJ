# 2022/12/18 정수론, 소수 판정
# https://www.acmicpc.net/problem/1241
import sys
input = sys.stdin.readline

N = int(input())
p = []
for i in range(N):
  p.append(int(input()))

res = [0] * N
# 각 숫자의 개수가 담긴 리스트 생성
number = [0] * (max(p) +1)
for i in p:
  number[i] += 1

for i in range(N):
  k = 1
  while k*k <= (p[i]):
    if p[i] % k == 0:
      # 같지 않으면 해당 수와 현재 값에서 그 수를 나눈 값을 더한다.
      # if i = 6, k = 2, res[6] += number[2] + number[3]
      if k*k != p[i]:
        res[i] += number[k] + number[p[i]//k]
      else: # 같으면 해당 수만큼 더한다
        res[i] += number[k]
    k += 1

# 자기 자신을 뺀 후 정답 출력
for i in res:
  print(i-1)