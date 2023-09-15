# 2023/07/19 Bruteforcing, TwoPointer, Sorting
# https://www.acmicpc.net/problem/28353
def two_pointer():
  s = 0
  e = N-1
  res = 0
  while s < e:
    if cat_weight[s] + cat_weight[e] <= K: # 두 고양이의 무게를 버틸 수 있는 경우
      res += 1
      s += 1
    e -= 1
  print(res) # 정답 출력

N, K = map(int,input().split())
cat_weight = sorted(list(map(int,input().split())))
two_pointer()