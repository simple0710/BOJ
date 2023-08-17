# 2023/07/20 PrefixSum
# https://www.acmicpc.net/problem/21921
N, X = map(int,input().split())
data = list(map(int,input().split()))

for i in range(1, N): # 누적합 계산
  data[i] = data[i] + data[i-1]

visitant = data[X-1] if data[X-1] != 0 else 0
day_cnt = 1
for i in range(X, N):
  check = data[i] - data[i-X]
  if check > visitant: # 최댓값을 찾은 경우
    day_cnt = 1
    visitant = check
  elif check == visitant: # 현재 값과 같은 경우
    day_cnt += 1

if visitant: # 방문자 최댓값이 1이상인 경우
  # 최대 방문자, 최대 방문자 만큼의 기간의 수
  print(visitant)
  print(day_cnt)
else: # 방문자의 값이 0인 경우
  print('SAD')