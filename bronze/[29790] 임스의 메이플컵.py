# 2023/09/08 Implementation
# https://www.acmicpc.net/problem/29790
N, U, L = map(int,input().split())
if N >= 1000: # 1000 문제 이상 해결한 경우
  # 유니온 레벨이 8000 이상이거나 최고 레벨이 260 이상인 경우
  if U >= 8000 or L >= 260:
    print('Very Good')
  else: # 그렇지 않은 경우
    print("Good")
else: # 1000 문제 미만으로 해결한 경우
  print("Bad")