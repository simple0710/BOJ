# 2023/04/01 Implementation, Simulation, Queue
# https://www.acmicpc.net/problem/5464
N, M = map(int,input().split())
price = []
for i in range(N): # 가격 추가
  price.append(int(input()))

car_w = []
for i in range(M): # 무게 추가
  car_w.append(int(input()))

park = [0] * N
wait = []
res = 0
for i in range(2 * M):
  cn = int(input()) # 자동차 번호
  if cn > 0: # 주차장으로 들어오는 경우
    for j in range(N):
      if park[j] == 0: # 주차 공간이 있는 경우
        park[j] = cn
        break
    else: # 주차 공간이 없는 경우
      wait.append(cn)
  else: # 주차장에서 나가는 경우
    ind = park.index(-cn)
    park[ind] = 0
    if wait: 
      park[ind] = wait.pop(0)
    # 비용 추가
    res += price[ind] * car_w[-cn-1]

# 정답 출력
print(res)