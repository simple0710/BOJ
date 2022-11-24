# 2022/11/24 조합론, 백트래킹
# 방법 1 : 조합론
from itertools import permutations
# 정보 입력
N = int(input())
arr = list(permutations(range(1, N+1), N)) # 조합
# 정답 출력
for i in arr:
  print(*i)

# 방법 2 : 백트래킹
def back():
  # 일정 길이에 도달한 경우 출력
  if len(s) == N:
    print(*s)
    return
  for i in range(1, N+1):
    # s에 없는 경우
    if i not in s:
      s.append(i)
      back()
      s.pop()

# 정보 입력
N = int(input())
s = []
# 백트래킹 시작
back()