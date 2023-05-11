# 2023/05/11 Greedy
# https://www.acmicpc.net/problem/5585
N = 1000 - int(input())
res = 0
for i in [500, 100, 50, 10, 5, 1]:
  res += N // i # 몫을 더한다
  N %= i
# 정답 출력
print(res)