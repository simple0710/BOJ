# 2023/04/11 TwoPointer, Sorting
# https://www.acmicpc.net/problem/1337
def two_pointer():
  check = 0
  res = 4
  s = 0
  e = 0
  while e < N:
    if data[e] - data[s] < 5: # 올바른 배열에 속한 경우
      check += 1
      e += 1
    else: # 올바른 배열에 속하지 않은 경우
      check -= 1
      s += 1
    res = min(res, 5 - check) # res와 5 - check 비교
  return res # 정답 반환

N = int(input())
data = sorted(list(int(input()) for _ in range(N)))
# 탐색 시작
res = two_pointer()
# 정답 출력
print(res)