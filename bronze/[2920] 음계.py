# 2023/08/03 Implementation
# https://www.acmicpc.net/problem/2920
data = list(map(int,input().split()))
if data == list(range(1, 9)): # 순서대로 연주한 경우
  print("ascending")
elif data == list(range(8, 0, -1)): # 역순으로 연주한 경우
  print("descending")
else: # 그 외의 경우
  print("mixed")