# 2023/02/16 Greedy
# https://www.acmicpc.net/problem/8980
N, C = map(int,input().split())
T = int(input())
box = []
for _ in range(T):
  no, trans, cnt = map(int,input().split())
  box.append([no, trans, cnt])

box.sort(key=lambda x: x[1]) # 도착 지점을 기준으로 정렬

my_box = [C] * (N+1)
res = 0
for s, e, b in box:
  check = C
  for i in range(s, e): # e에 도착하기 전에 들고 있을 수 있는 박스의 개수 저장
    check = min(check, my_box[i])
  check = min(check, b) # 들고 있을 수 있는 박스의 개수와 현재 박스의 개수 중 가장 작은 값을 check로 한다
  for i in range(s, e): # 목적지까지 도착할 때까지 해당 공간에서 가지고 있을 수 있는 박스의 값을 구한다.
    my_box[i] -= check
  
  # 배송한 값 더하기
  res += check

# 정답 출력
print(res)