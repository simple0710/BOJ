# 2023/08/06 Implementation
# https://www.acmicpc.net/problem/28431
data = dict()
for _ in range(5):
  N = int(input())
  # 양말 숫자에 맞는 딕셔너리 값을 증가 시킨다.
  if N not in data.keys():
    data[N] = 1
  else:
    data[N] += 1
for i in data.keys():
  if data[i] % 2 == 1: # 하나가 남는 경우 정답 출력
    print(i)