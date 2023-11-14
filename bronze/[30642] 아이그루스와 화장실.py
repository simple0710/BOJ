# 2023/11/11 Math, Implementation
# https://www.acmicpc.net/problem/30642
input() # 동아리방의 층수
name = input() # 마스코트 이름
K=int(input()) # 마스코트가 있는 층
if name == "annyong": # 안뇽이인 경우
  if K % 2 == 0: # 본인 화장실의 층이 아닌 경우
    K-= 1
else: # 인덕이인 경우
  if K % 2 == 1: # 본인 화장실의 층이 아닌 경우
    if K == 1: # 바닥층이면 윗층으로 간다
      K += 1
    else: # 아래층으로 간다.
      K -= 1
print(K) # 가장 가까운 화장실 출력