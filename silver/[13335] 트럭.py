n, w, L = map(int,input().split()) # 버스 수, 다리 길이, 최대하중
bus = list(map(int,input().split())) # 버스 무게

b = [0] * w
time = 0 
while b: # 버스가 들어오고 마지막 버스가 빠져나갈 때 까지
  time += 1
  b.pop(0) # 다리 첫번째 요소 pop
  if bus: # 트럭이 존재할 때
    # 현재 다리 무게 + bus 무게가 최대 하중보다 낮으면 해당 bus 추가
    if sum(b) + bus[0] <= L:
      b.append(bus.pop(0))
    # 아니면 진행
    else:
      b.append(0)

print(time)