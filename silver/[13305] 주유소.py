# 2023/01/25 그리디
# https://www.acmicpc.net/problem/13305
import sys
input = sys.stdin.readline

N = int(input())
dis = list(map(int,input().split()))
pay = list(map(int,input().split()))
# 풀이 1
res = 0
now = pay.pop(0)
total_dis = 0
while dis:
  next = pay.pop(0)
  total_dis += dis.pop(0)
  if now > next: # 현재 비용이 더 큰 경우 계산 후 이동
    res += total_dis * now
    total_dis = 0
    now = next
res += total_dis * now

# 정답 출력
print(res)

# 풀이 2
res = 0
m = pay[0]
for i in range(N-1):
  if pay[i] < m:
    m = pay[i]
  res += m * dis[i]

# 정답 출력
print(res)