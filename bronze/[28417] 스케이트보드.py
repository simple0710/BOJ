# 2023/07/29 Math, Implementation, Sorting
# https://www.acmicpc.net/problem/28417
res = 0
for _ in range(int(input())):
  data = list(map(int,input().split()))
  # 가장 높은 점수로 갱신한다.
  # 두 차례의 런 중 최고 점수 + 다섯 차례의 트릭 연기 중 상위 2개의 점수의 합
  res = max(res, max(data[0], data[1]) + sum(sorted(data[2:])[-2:]))
print(res) # 정답 출력