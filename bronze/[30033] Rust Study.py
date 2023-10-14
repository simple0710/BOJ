# 2023/09/16 Implementation
# https://www.acmicpc.net/problem/30033
N = int(input())
data = list(map(int,input().split())) # 공부를 계획한 페이지 수
data2 = list(map(int,input().split())) # 공부한 페이지 수
# 계획한 페이지 수 이상으로 공부한 횟수를 구한다.
res = 0
for i in range(N):
  if data[i] <= data2[i]:
    res += 1
print(res) # 정답 출력