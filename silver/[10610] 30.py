# 2023/05/12 Math, String, Greedy, Sorting
# https://www.acmicpc.net/problem/10610
N = input()
N = sorted(N, reverse=True)

check = 0
if '0' not in N: # 0이 없는 경우
  print(-1)
else:
  for i in N:
    check += int(i)
  if check % 3 != 0: # 3의 배수가 아닌 경우
    print(-1)
  else:
    # 정답 출력
    print(''.join(N))