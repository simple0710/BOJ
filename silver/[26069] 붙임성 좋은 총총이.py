# 2022/12/17 자료 구조
# https://www.acmicpc.net/problem/26069
N = int(input())
dance = ['ChongChong']
# 양쪽 비교 후 dance 안에 있는 사람이 있고,
# dance 안에 없는 사람을 dance에 추가
for _ in range(N):
  a, b = map(str, input().split())
  if a in dance:
    if b not in dance:
      dance.append(b)
  elif b in dance:
    if a not in dance:
      dance.append(a)
# 정답 출력
print(len(dance))