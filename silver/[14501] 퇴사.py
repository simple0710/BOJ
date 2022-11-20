# 2022/11/18 DP
data = []
day = int(input())
for _ in range(day):
  x, y = map(int,input().split())
  data.append((x, y))

dp = [0] * (day + 1)
for i in range(day - 1, -1, -1):
  # i일에 상담을 하는 것이 퇴사일을 넘기면 상담을 하지 않는다.
  if i + data[i][0] > day:
    dp[i] = dp[i + 1]
  # i일에 상담을 하는 것과 상담을 안하는 것 중 큰 것을 선택한다.
  else:
    dp[i] = max(dp[i + 1], data[i][1] + dp[i + data[i][0]])
# 정답 출력
print(dp[0])

# 다른 풀이
'''
import sys
input = sys.stdin.readline
n = int(input())
# n일까지 벌 수 있는 최대수익을 저장
d = [0] * 20
tplist = [[0,0]]
for _ in range(n):
  t, p = map(int,input().split())
  tplist.append([t, p])

for i in range(1,n+1):
  x = tplist[i][0] - 1
  d[i] = max(d[i - 1],d[i])
  d[i + x] = max(d[i - 1] + tplist[i][1], d[i + x])
  
print(d[n])
'''