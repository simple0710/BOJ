# 2023/06/27 Math
# https://www.acmicpc.net/problem/4344
for _ in range(int(input())):
  data = list(map(int,input().split()))
  average = sum(data[1:]) / data[0] # 평균
  cnt = 0
  for i in data[1:]:
    if i > average: # 평균을 넘는 학생의 수를 구하낟.
      cnt += 1
  # 평균을 넘는 학생의 수의 비율(소수점 4번째 자리에서 반올림)을 구한다.
  print(f'{cnt * 100 / data[0] :.3f}%')