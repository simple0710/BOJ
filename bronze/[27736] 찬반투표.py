# 2023/03/11 구현
# https://www.acmicpc.net/problem/27736
N = int(input())
arr = list(map(int,input().split()))
t = arr.count(1)
f = arr.count(-1)
m = arr.count(0)
if m * 2 >= N: # 기권 수가 절반 이상인 경우
  print("INVALID")
elif t > f: # 찬성이 더 많은 경우
  print("APPROVED")
else: # 반대가 더 많은 경우
  print("REJECTED")