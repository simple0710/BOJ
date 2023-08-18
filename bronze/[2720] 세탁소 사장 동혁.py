# 2023/06/23 Math, Greedy
# https://www.acmicpc.net/problem/2720
for _ in range(int(input())):
  C = int(input())
  for i in [25, 10, 5, 1]:
    # 정답(몫) 출력
    print(C // i, end=' ')
    C %= i # 나머지 계산
  print()